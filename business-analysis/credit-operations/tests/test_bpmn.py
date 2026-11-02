"""Validar BPMN 2.0 XML e coerência estrutural dos diagramas.
Execução: python tests/test_bpmn.py
Usa apenas a biblioteca padrão. Não substitui BPMN Modeler nem um validador XSD oficial.
"""
from pathlib import Path
from collections import Counter, defaultdict
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
NS = {
    "b": "http://www.omg.org/spec/BPMN/20100524/MODEL",
    "di": "http://www.omg.org/spec/BPMN/20100524/DI",
}
B = "{" + NS["b"] + "}"
DI = "{" + NS["di"] + "}"
NODE_TAGS = {
    "startEvent", "endEvent", "task", "userTask", "serviceTask",
    "sendTask", "receiveTask", "exclusiveGateway", "boundaryEvent",
}

for filename in ("AS-IS.bpmn", "TO-BE.bpmn"):
    tree = ET.parse(ROOT / "bpmn" / filename)
    root = tree.getroot()

    by_id = {}
    for elem in root.iter():
        elem_id = elem.get("id")
        if elem_id:
            assert elem_id not in by_id, f"{filename}: duplicate id {elem_id}"
            by_id[elem_id] = elem

    processes = root.findall("b:process", NS)
    collaborations = root.findall("b:collaboration", NS)
    assert len(processes) == 1 and len(collaborations) == 1
    process, collaboration = processes[0], collaborations[0]
    assert process.get("isExecutable") == "false"

    participants = collaboration.findall("b:participant", NS)
    assert len(participants) == 3
    assert sum(p.get("processRef") == process.get("id") for p in participants) == 1
    participant_ids = {p.get("id") for p in participants}

    node_ids = {e.get("id") for e in process.iter() if e.tag.removeprefix(B) in NODE_TAGS}
    lane_refs = []
    for lane in process.findall(".//b:lane", NS):
        lane_refs.extend(ref.text for ref in lane.findall("b:flowNodeRef", NS))
    assert len(lane_refs) == len(node_ids)
    assert Counter(lane_refs) == Counter(node_ids)

    flows = process.findall("b:sequenceFlow", NS)
    messages = collaboration.findall("b:messageFlow", NS)
    incoming, outgoing = defaultdict(int), defaultdict(int)
    for flow in flows:
        source, target = flow.get("sourceRef"), flow.get("targetRef")
        assert source in node_ids and target in node_ids
        outgoing[source] += 1
        incoming[target] += 1
    for message in messages:
        assert message.get("sourceRef") in node_ids | participant_ids
        assert message.get("targetRef") in node_ids | participant_ids
        assert message.get("sourceRef") != message.get("targetRef")
        # Comunicação entre organizações; nunca entre duas atividades do mesmo processo.
        assert (message.get("sourceRef") in participant_ids) != (message.get("targetRef") in participant_ids)

    for node in process.iter():
        if node.get("id") not in node_ids:
            continue
        n = node.get("id")
        if node.tag == B + "startEvent":
            assert incoming[n] == 0 and outgoing[n] >= 1
        elif node.tag == B + "endEvent":
            assert outgoing[n] == 0 and incoming[n] >= 1
        elif node.tag == B + "boundaryEvent":
            assert node.get("attachedToRef") in node_ids
            assert incoming[n] == 0 and outgoing[n] >= 1
        else:
            assert incoming[n] >= 1 and outgoing[n] >= 1, n
        if node.tag == B + "exclusiveGateway":
            assert outgoing[n] == 2, (n, outgoing[n])
            assert node.get("default") in {f.get("id") for f in flows if f.get("sourceRef") == n}

    shapes = {e.get("bpmnElement") for e in root.findall(".//di:BPMNShape", NS)}
    edges = {e.get("bpmnElement") for e in root.findall(".//di:BPMNEdge", NS)}
    assert node_ids <= shapes
    assert participant_ids <= shapes
    assert {e.get("id") for e in flows + messages} <= edges
    assert all(ref in by_id for ref in shapes | edges)

    if filename == "TO-BE.bpmn":
        timers = process.findall("b:boundaryEvent", NS)
        assert len(timers) == 1 and timers[0].get("cancelActivity") == "false"
        assert timers[0].find("b:timerEventDefinition", NS) is not None

    print(
        f"PASS {filename}: 3 pools, "
        f"{len(process.findall('.//b:lane', NS))} lanes, "
        f"{len(node_ids)} nodes, {len(flows)} sequence flows, "
        f"{len(messages)} message flows, DI present"
    )
print("Nota: validar a renderização e as regras de negócio num modelador antes de produção.")

---
entity_id: "protein.P03819"
entity_type: "protein"
name: "kefC"
source_database: "UniProt"
source_id: "P03819"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01413, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2046548}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01413, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2046548}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "kefC trkC b0047 JW0046"
---

# kefC

`protein.P03819`

## Static

- Type: `protein`
- Source: `UniProt:P03819`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell inner membrane {ECO:0000255|HAMAP-Rule:MF_01413, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2046548}; Multi-pass membrane protein {ECO:0000255|HAMAP-Rule:MF_01413, ECO:0000269|PubMed:15919996, ECO:0000269|PubMed:2046548}.

## Enriched Summary

FUNCTION: Pore-forming subunit of a potassium efflux system that confers protection against electrophiles. Catalyzes K(+)/H(+) antiport. Can also export rubidium, lithium and sodium. {ECO:0000255|HAMAP-Rule:MF_01413, ECO:0000269|PubMed:17679694, ECO:0000269|PubMed:21041667, ECO:0000269|PubMed:9023177}. KefB and KefC are two independent glutathione-regulated potassium efflux systems, which play a role in protecting the cell from electrophile toxicity. Mutations in kefB and kefC affect potassium efflux at neutral pH, can be complemented by the cloned genes and probably function via potassium/proton antiport . Potassium efflux by KefB or KefC is activated by adducts formed by reaction of glutathione with electrophilic compounds such as N-ethylmaleimide, methylglyoxal and chlorodinitrobenzene . Potassium efflux mediated by KefB and KefC leads to acidification of the cytoplasm, which protects the cell from electrophile toxicity . KefB and KefC differ in their activation by methylglyoxal, with KefC only weakly activated . KefC is a member of the CPA2 family of monovalent cation/proton antiporters. The ancillary protein, KefF, is required for maximum activity of KefC . In addition to KefB and KefC, additional unidentified potassium efflux systems exist. KefC consists of a membrane domain attached to a C-terminal KTN (K+ transport, nucleotide binding) domain via a flexible linker...

## Biological Role

Component of K+ : H+ antiporter KefC (complex.ecocyc.CPLX0-7819).

## Annotation

FUNCTION: Pore-forming subunit of a potassium efflux system that confers protection against electrophiles. Catalyzes K(+)/H(+) antiport. Can also export rubidium, lithium and sodium. {ECO:0000255|HAMAP-Rule:MF_01413, ECO:0000269|PubMed:17679694, ECO:0000269|PubMed:21041667, ECO:0000269|PubMed:9023177}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-7819|complex.ecocyc.CPLX0-7819]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0047|gene.b0047]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P03819`
- `KEGG:ecj:JW0046;eco:b0047;ecoc:C3026_00245;`
- `GeneID:944773;`
- `GO:GO:0000166; GO:0005886; GO:0006813; GO:0006885; GO:0009636; GO:0015503; GO:0015643; GO:0016020; GO:0019899; GO:0042542; GO:0042803; GO:0051453; GO:0051454; GO:0051595; GO:1902600; GO:1903103`

## Notes

Glutathione-regulated potassium-efflux system protein KefC (K(+)/H(+) antiporter)

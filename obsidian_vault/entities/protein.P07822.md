---
entity_id: "protein.P07822"
entity_type: "protein"
name: "fhuD"
source_database: "UniProt"
source_id: "P07822"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:17218314}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "fhuD b0152 JW0148"
---

# fhuD

`protein.P07822`

## Static

- Type: `protein`
- Source: `UniProt:P07822`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:17218314}.

## Enriched Summary

FUNCTION: Part of the ABC transporter complex FhuCDB involved in iron(3+)-hydroxamate import. Binds the iron(3+)-hydroxamate complex and transfers it to the membrane-bound permease. Required for the transport of all iron(3+)-hydroxamate siderophores such as ferrichrome, gallichrome, desferrioxamine, coprogen, aerobactin, shizokinen, rhodotorulic acid and the antibiotic albomycin. {ECO:0000269|PubMed:10742172, ECO:0000269|PubMed:11805094, ECO:0000269|PubMed:2254301, ECO:0000269|PubMed:34887516, ECO:0000269|PubMed:8522527}. FhuD is the periplasmic siderophore binding component of an iron(III) hydroxamate ABC transporter. Purified FhuD binds ferrichrome (Kd = 1 µM), ferric coprogen (Kd = 0.3 µM), ferric aerobactin (Kd = 0.4 µM) and the antibiotic albomycin (Kd = 5.4 µM). It also binds ferrichrome A, ferrioxamine B and ferrioxamine E with lower affinity (Kd = 79, 36, and 42 µM, respectively) . Peptide mapping experiments suggest that FhuD binds to periplasmic loop 2, cytoplasmic loop 7 and the transmembrane region of FhuB...

## Biological Role

Component of Fe(3+) hydroxamate ABC transporter (complex.ecocyc.ABC-11-CPLX).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

FUNCTION: Part of the ABC transporter complex FhuCDB involved in iron(3+)-hydroxamate import. Binds the iron(3+)-hydroxamate complex and transfers it to the membrane-bound permease. Required for the transport of all iron(3+)-hydroxamate siderophores such as ferrichrome, gallichrome, desferrioxamine, coprogen, aerobactin, shizokinen, rhodotorulic acid and the antibiotic albomycin. {ECO:0000269|PubMed:10742172, ECO:0000269|PubMed:11805094, ECO:0000269|PubMed:2254301, ECO:0000269|PubMed:34887516, ECO:0000269|PubMed:8522527}.

## Pathways

- `eco02010` ABC transporters (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.ABC-11-CPLX|complex.ecocyc.ABC-11-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1 | EcoCyc transporter component coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b0152|gene.b0152]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P07822`
- `KEGG:ecj:JW0148;eco:b0152;ecoc:C3026_00690;`
- `GeneID:75170052;947510;`
- `GO:GO:0015687; GO:0030288; GO:0055052; GO:0098711`

## Notes

Iron(3+)-hydroxamate-binding protein FhuD (Ferric hydroxamate uptake protein D) (Ferrichrome-binding periplasmic protein) (Iron(III)-hydroxamate-binding protein FhuD)

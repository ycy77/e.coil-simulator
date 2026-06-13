---
entity_id: "protein.P32155"
entity_type: "protein"
name: "frvA"
source_database: "UniProt"
source_id: "P32155"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "frvA yiiK b3900 JW3871"
---

# frvA

`protein.P32155`

## Static

- Type: `protein`
- Source: `UniProt:P32155`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000305}.

## Enriched Summary

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FrvAB PTS system is involved in fructose transport. {ECO:0000305|PubMed:8019415}. frvA is predicted to encode a hydrophilic protein with similarity to the IIA domain of the PTS Enzyme IIs specific for mannitol and fructose. FrvA contains a conserved histidine (His64) .

## Biological Role

Component of putative PTS enzyme II FrvAB (complex.ecocyc.CPLX-159).

## Annotation

FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FrvAB PTS system is involved in fructose transport. {ECO:0000305|PubMed:8019415}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX-159|complex.ecocyc.CPLX-159]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b3900|gene.b3900]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32155`
- `KEGG:ecj:JW3871;eco:b3900;`
- `GeneID:75204574;948391;`
- `GO:GO:0005737; GO:0008982; GO:0009401; GO:0016301; GO:1902495; GO:1990539`

## Notes

PTS system fructose-like EIIA component (Fructose-like phosphotransferase enzyme IIA component)

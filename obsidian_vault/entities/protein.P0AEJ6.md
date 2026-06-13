---
entity_id: "protein.P0AEJ6"
entity_type: "protein"
name: "eutB"
source_database: "UniProt"
source_id: "P0AEJ6"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000255|HAMAP-Rule:MF_00861}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eutB b2441 JW2434"
---

# eutB

`protein.P0AEJ6`

## Static

- Type: `protein`
- Source: `UniProt:P0AEJ6`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000255|HAMAP-Rule:MF_00861}.

## Enriched Summary

FUNCTION: Catalyzes the deamination of various vicinal amino-alcohols to oxo compounds (PubMed:19762342). Allows this organism to utilize ethanolamine as the sole source of nitrogen and carbon in the presence of external vitamin B12. It is spontaneously inactivated by its substrate and reactivated by EutA (PubMed:15466038). {ECO:0000269|PubMed:15466038, ECO:0000269|PubMed:19762342, ECO:0000305|PubMed:2197274}.

## Biological Role

Catalyzes ethanolamine ammonia-lyase (acetaldehyde-forming) (reaction.R00749). Component of ethanolamine ammonia-lyase (complex.ecocyc.ETHAMLY-CPLX).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the deamination of various vicinal amino-alcohols to oxo compounds (PubMed:19762342). Allows this organism to utilize ethanolamine as the sole source of nitrogen and carbon in the presence of external vitamin B12. It is spontaneously inactivated by its substrate and reactivated by EutA (PubMed:15466038). {ECO:0000269|PubMed:15466038, ECO:0000269|PubMed:19762342, ECO:0000305|PubMed:2197274}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00749|reaction.R00749]] `KEGG` `database` - via EC:4.3.1.7
- `is_component_of` --> [[complex.ecocyc.ETHAMLY-CPLX|complex.ecocyc.ETHAMLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2441|gene.b2441]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AEJ6`
- `KEGG:ecj:JW2434;eco:b2441;ecoc:C3026_13555;`
- `GeneID:75172555;75204289;946924;`
- `GO:GO:0005829; GO:0006520; GO:0008851; GO:0009350; GO:0031419; GO:0031471; GO:0046336`
- `EC:4.3.1.7`

## Notes

Ethanolamine ammonia-lyase large subunit (EAL large subunit) (EC 4.3.1.7) (Ethanolamine ammonia-lyase alpha subunit) (Ethanolamine ammonia-lyase heavy chain) (Ethanolamine deaminase large subunit)

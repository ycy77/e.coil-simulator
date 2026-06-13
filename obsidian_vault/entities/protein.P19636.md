---
entity_id: "protein.P19636"
entity_type: "protein"
name: "eutC"
source_database: "UniProt"
source_id: "P19636"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000255|HAMAP-Rule:MF_00601}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "eutC b2440 JW2433"
---

# eutC

`protein.P19636`

## Static

- Type: `protein`
- Source: `UniProt:P19636`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Bacterial microcompartment {ECO:0000255|HAMAP-Rule:MF_00601}.

## Enriched Summary

FUNCTION: Catalyzes the deamination of various vicinal amino-alcohols to oxo compounds (PubMed:19762342). Ethanolamine ammonia-lyase (EAL) allows bacteria to utilize ethanolamine as the sole source of nitrogen and carbon in the presence of external vitamin B12. It is spontaneously inactivated by its substrate and reactivated by EutA (PubMed:15466038). Directly targeted to the BMC. May play a role in bacterial microcompartment (BMC) assembly or maintenance (By similarity). {ECO:0000250|UniProtKB:P19265, ECO:0000269|PubMed:15466038, ECO:0000269|PubMed:19762342, ECO:0000305|PubMed:2197274}. An E. coli BW25113 mutant, which had the interrupting prophage between eutA and eutB removed, grows similarly to the E. coli K-12 strain W3110, which lacks the prophage in its eut transcription unit, when provided with ethanolamine (EA) as the sole nitrogen source . Further experiments to analyze ethanolamine utilization and the microcompartments were carried out in the E. coli W3110 strain. A GFP-tagged eutC strain of W3110 formed distinct puncta of irregular polyhedrals surrounded by a shell layer with sharp edges and vertices observed by fluorescent microscopy and cryo-electron tomography, likely representing the ethanolamine utilization microcompartments...

## Biological Role

Catalyzes ethanolamine ammonia-lyase (acetaldehyde-forming) (reaction.R00749). Component of ethanolamine ammonia-lyase (complex.ecocyc.ETHAMLY-CPLX).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Catalyzes the deamination of various vicinal amino-alcohols to oxo compounds (PubMed:19762342). Ethanolamine ammonia-lyase (EAL) allows bacteria to utilize ethanolamine as the sole source of nitrogen and carbon in the presence of external vitamin B12. It is spontaneously inactivated by its substrate and reactivated by EutA (PubMed:15466038). Directly targeted to the BMC. May play a role in bacterial microcompartment (BMC) assembly or maintenance (By similarity). {ECO:0000250|UniProtKB:P19265, ECO:0000269|PubMed:15466038, ECO:0000269|PubMed:19762342, ECO:0000305|PubMed:2197274}.

## Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00749|reaction.R00749]] `KEGG` `database` - via EC:4.3.1.7
- `is_component_of` --> [[complex.ecocyc.ETHAMLY-CPLX|complex.ecocyc.ETHAMLY-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=6 | EcoCyc protcplxs.col coefficient=6

## Incoming Edges (1)

- `encodes` <-- [[gene.b2440|gene.b2440]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P19636`
- `KEGG:ecj:JW2433;eco:b2440;ecoc:C3026_13550;`
- `GeneID:946925;`
- `GO:GO:0006520; GO:0008851; GO:0009350; GO:0031419; GO:0031471; GO:0046336`
- `EC:4.3.1.7`

## Notes

Ethanolamine ammonia-lyase small subunit (EAL small subunit) (EC 4.3.1.7) (Ethanolamine ammonia-lyase beta subunit) (Ethanolamine ammonia-lyase light chain) (Ethanolamine deaminase small subunit)

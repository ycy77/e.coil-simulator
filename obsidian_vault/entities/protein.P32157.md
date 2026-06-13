---
entity_id: "protein.P32157"
entity_type: "protein"
name: "yiiM"
source_database: "UniProt"
source_id: "P32157"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "yiiM b3910 JW5559"
---

# yiiM

`protein.P32157`

## Static

- Type: `protein`
- Source: `UniProt:P32157`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Reductase involved in the detoxification of N-hydroxylated base analogs (PubMed:18312271). Contributes to the detoxification of 6-N-hydroxylaminopurine (HAP) by catalyzing the reduction of HAP to adenine (PubMed:18312271, PubMed:34921810). Is specific for N-hydroxylated substrates over N-oxides or sulfoxides (PubMed:34921810). In the presence of methyl viologen as reduced electron donor, it preferentially reduces N-hydroxylated compounds such as hydroxylamines, amidoximes, N-hydroxypurines and N-hydroxyureas but shows little or no activity against amine-oxides or sulfoxides (PubMed:34921810). YiiM is not involved in molybdenum cofactor (MoCo) biosynthesis or in MoCo sulfuration (PubMed:18312271). {ECO:0000269|PubMed:18312271, ECO:0000269|PubMed:34921810}.

## Biological Role

Component of 6-hydroxyaminopurine reductase (complex.ecocyc.CPLX0-8259).

## Annotation

FUNCTION: Reductase involved in the detoxification of N-hydroxylated base analogs (PubMed:18312271). Contributes to the detoxification of 6-N-hydroxylaminopurine (HAP) by catalyzing the reduction of HAP to adenine (PubMed:18312271, PubMed:34921810). Is specific for N-hydroxylated substrates over N-oxides or sulfoxides (PubMed:34921810). In the presence of methyl viologen as reduced electron donor, it preferentially reduces N-hydroxylated compounds such as hydroxylamines, amidoximes, N-hydroxypurines and N-hydroxyureas but shows little or no activity against amine-oxides or sulfoxides (PubMed:34921810). YiiM is not involved in molybdenum cofactor (MoCo) biosynthesis or in MoCo sulfuration (PubMed:18312271). {ECO:0000269|PubMed:18312271, ECO:0000269|PubMed:34921810}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8259|complex.ecocyc.CPLX0-8259]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b3910|gene.b3910]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P32157`
- `KEGG:ecj:JW5559;eco:b3910;ecoc:C3026_21145;`
- `GeneID:75174151;948406;`
- `GO:GO:0005829; GO:0009407; GO:0009636; GO:0016491; GO:0016661; GO:0030151; GO:0030170; GO:0042803`
- `EC:1.-.-.-`

## Notes

6-hydroxylaminopurine reductase YiiM (EC 1.-.-.-) (Hydroxylaminopurine resistance protein YiiM)

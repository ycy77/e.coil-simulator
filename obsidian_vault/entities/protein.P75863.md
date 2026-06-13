---
entity_id: "protein.P75863"
entity_type: "protein"
name: "ycbX"
source_database: "UniProt"
source_id: "P75863"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ycbX b0947 JW5126"
---

# ycbX

`protein.P75863`

## Static

- Type: `protein`
- Source: `UniProt:P75863`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Reductase involved in the detoxification of N-hydroxylated base analogs (PubMed:18312271). Contributes to the detoxification of 6-N-hydroxylaminopurine (HAP) by catalyzing the reduction of HAP to adenine (PubMed:18312271, PubMed:35640667). In the presence of methyl viologen as reduced electron donor, it is also active toward other N-hydroxy substrates such as 2-amino-6-hydroxylaminopurine (2-AHAP), N-hydroxyadenosine, N-hydroxyacetamidine, N-hydroxyurea and hydroxylamine, but it cannot use N-oxide and sulfoxide substrates, or nitrate and chlorate (PubMed:35640667). The reducing equivalents required for the detoxification reaction may be provided by the sulfite reductase component CysJ, which functions as a partner of YcbX (PubMed:20118259). YcbX is not involved in molybdenum cofactor (MoCo) biosynthesis or in MoCo sulfuration (PubMed:18312271). {ECO:0000269|PubMed:18312271, ECO:0000269|PubMed:20118259, ECO:0000269|PubMed:35640667}.

## Biological Role

Component of 6-N-hydroxylaminopurine resistance protein (complex.ecocyc.CPLX0-10380).

## Annotation

FUNCTION: Reductase involved in the detoxification of N-hydroxylated base analogs (PubMed:18312271). Contributes to the detoxification of 6-N-hydroxylaminopurine (HAP) by catalyzing the reduction of HAP to adenine (PubMed:18312271, PubMed:35640667). In the presence of methyl viologen as reduced electron donor, it is also active toward other N-hydroxy substrates such as 2-amino-6-hydroxylaminopurine (2-AHAP), N-hydroxyadenosine, N-hydroxyacetamidine, N-hydroxyurea and hydroxylamine, but it cannot use N-oxide and sulfoxide substrates, or nitrate and chlorate (PubMed:35640667). The reducing equivalents required for the detoxification reaction may be provided by the sulfite reductase component CysJ, which functions as a partner of YcbX (PubMed:20118259). YcbX is not involved in molybdenum cofactor (MoCo) biosynthesis or in MoCo sulfuration (PubMed:18312271). {ECO:0000269|PubMed:18312271, ECO:0000269|PubMed:20118259, ECO:0000269|PubMed:35640667}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-10380|complex.ecocyc.CPLX0-10380]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0947|gene.b0947]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P75863`
- `KEGG:ecj:JW5126;eco:b0947;ecoc:C3026_05800;`
- `GeneID:945563;`
- `GO:GO:0003824; GO:0009407; GO:0009636; GO:0030151; GO:0030170; GO:0051537`
- `EC:1.-.-.-`

## Notes

6-hydroxylaminopurine reductase YcbX (EC 1.-.-.-) (Hydroxylaminopurine resistance molybdoenzyme YcbX)

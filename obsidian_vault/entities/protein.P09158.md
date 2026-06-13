---
entity_id: "protein.P09158"
entity_type: "protein"
name: "speE"
source_database: "UniProt"
source_id: "P09158"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00198}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "speE b0121 JW0117"
---

# speE

`protein.P09158`

## Static

- Type: `protein`
- Source: `UniProt:P09158`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00198}.

## Enriched Summary

FUNCTION: Involved in the biosynthesis of polyamines which play a significant role in the structural and functional organization in the chromoid of E.coli by compacting DNA and neutralizing negative charges. Catalyzes the irreversible transfer (ping-pong mechanism) of a propylamine group from the amino donor S-adenosylmethioninamine (decarboxy-AdoMet) to putrescine (1,4-diaminobutane) to yield spermidine. Cadaverine (1,5-diaminopentane) and spermidine can also be used as the propylamine acceptor. {ECO:0000269|PubMed:23001854, ECO:0000269|PubMed:4572733}.

## Biological Role

Component of spermidine synthase (complex.ecocyc.SPERMIDINESYN-CPLX).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

FUNCTION: Involved in the biosynthesis of polyamines which play a significant role in the structural and functional organization in the chromoid of E.coli by compacting DNA and neutralizing negative charges. Catalyzes the irreversible transfer (ping-pong mechanism) of a propylamine group from the amino donor S-adenosylmethioninamine (decarboxy-AdoMet) to putrescine (1,4-diaminobutane) to yield spermidine. Cadaverine (1,5-diaminopentane) and spermidine can also be used as the propylamine acceptor. {ECO:0000269|PubMed:23001854, ECO:0000269|PubMed:4572733}.

## Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.SPERMIDINESYN-CPLX|complex.ecocyc.SPERMIDINESYN-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b0121|gene.b0121]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P09158`
- `KEGG:ecj:JW0117;eco:b0121;ecoc:C3026_00510;`
- `GeneID:75202064;947726;`
- `GO:GO:0004766; GO:0005829; GO:0008295; GO:0010487; GO:0016768; GO:0042803; GO:0043918`
- `EC:2.5.1.-; 2.5.1.16; 2.5.1.22; 2.5.1.79`

## Notes

Polyamine aminopropyltransferase (Cadaverine aminopropyltransferase) (EC 2.5.1.-) (Putrescine aminopropyltransferase) (PAPT) (Spermidine aminopropyltransferase) (EC 2.5.1.79) (Spermidine synthase) (SPDS) (SPDSY) (EC 2.5.1.16) (Spermine synthase) (EC 2.5.1.22) (Thermospermine synthase)

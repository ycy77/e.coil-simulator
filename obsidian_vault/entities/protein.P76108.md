---
entity_id: "protein.P76108"
entity_type: "protein"
name: "ydcS"
source_database: "UniProt"
source_id: "P76108"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:18640095}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "ydcS b1440 JW1435"
---

# ydcS

`protein.P76108`

## Static

- Type: `protein`
- Source: `UniProt:P76108`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:18640095}.

## Enriched Summary

FUNCTION: Catalyzes the formation of short polymers of R-3-hydroxybutyrate (cPHB) (PubMed:18640095). Involved in natural transformation (PubMed:26826386). Probably part of the ABC transporter complex YdcSTUV. During natural transformation, may bind dsDNA and convey it to the inner membrane channel formed by YdcV (Probable). {ECO:0000269|PubMed:18640095, ECO:0000269|PubMed:26826386, ECO:0000305|PubMed:26826386}. The periplasmic protein,YdcS is a predicted to be the binding protein of an uncharacterized ABC transporter . YdcS is implicated in double strand (ds) DNA transport across the inner membrane during natural and chemical transformation; a ydcS deletion mutant has significantly decreased rates of natural and chemical transformation compared to wild type . Purified YdcS has poly-3-hydroxybutyrate (PHB) synthase activity; a ydcS deletion mutant contains approximately 30% less PHB complexed to proteins (cPHB) in the outer membrane compared to wild type; the addition of PHB to outer membrane proteins in the periplasm may facilitate their insertion into the outer membrane (see also ). Deletion of ydcS is associated with significant changes in the distribution of carbon fluxes in central metabolism ydcS is the first gene in a five gene operon (ydcSTUVpatD); transcription is initiated by σs containing RNA polymerase and induced under nitrogen limited growth...

## Biological Role

Catalyzes RXN1-42 (reaction.ecocyc.RXN1-42). Component of putative transport complex, ABC superfamily (complex.ecocyc.ABC-51-CPLX).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

FUNCTION: Catalyzes the formation of short polymers of R-3-hydroxybutyrate (cPHB) (PubMed:18640095). Involved in natural transformation (PubMed:26826386). Probably part of the ABC transporter complex YdcSTUV. During natural transformation, may bind dsDNA and convey it to the inner membrane channel formed by YdcV (Probable). {ECO:0000269|PubMed:18640095, ECO:0000269|PubMed:26826386, ECO:0000305|PubMed:26826386}.

## Pathways

- `eco02024` Quorum sensing (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.ecocyc.RXN1-42|reaction.ecocyc.RXN1-42]] `EcoCyc` `database` - EcoCyc enzymatic reaction
- `is_component_of` --> [[complex.ecocyc.ABC-51-CPLX|complex.ecocyc.ABC-51-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1

## Incoming Edges (1)

- `encodes` <-- [[gene.b1440|gene.b1440]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P76108`
- `KEGG:ecj:JW1435;eco:b1440;ecoc:C3026_08380;`
- `GeneID:75171521;946005;`
- `GO:GO:0009290; GO:0015847; GO:0016020; GO:0016746; GO:0019809; GO:0019810; GO:0030288; GO:0042619; GO:0055052; GO:0055085`
- `EC:2.3.1.-`

## Notes

Bifunctional polyhydroxybutyrate synthase / ABC transporter periplasmic binding protein (Poly-3-hydroxybutyrate synthase) (PHB synthase) (EC 2.3.1.-) (cPHB synthase)

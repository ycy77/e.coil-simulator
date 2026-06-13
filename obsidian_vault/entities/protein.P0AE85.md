---
entity_id: "protein.P0AE85"
entity_type: "protein"
name: "cpxP"
source_database: "UniProt"
source_id: "P0AE85"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:25207645, ECO:0000269|PubMed:9473036}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "cpxP yiiO b4484 JW5558"
---

# cpxP

`protein.P0AE85`

## Static

- Type: `protein`
- Source: `UniProt:P0AE85`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Periplasm {ECO:0000269|PubMed:25207645, ECO:0000269|PubMed:9473036}.

## Enriched Summary

FUNCTION: Acts as an auxiliary protein in the Cpx two-component envelope stress response system, helping modulate the Cpx response systems response to some inducers (PubMed:16303867, PubMed:25207645). Binds the periplasmic domain of sensor histidine kinase CpxA, inhibiting induction of the Cpx envelope stress response in the absence of inducer; overexpression decreases Cpx pathway activity (PubMed:16166523, PubMed:21317318). Some periplasmic stimulii (shown for P pili subunit PapE and probably 0.3 M NaCl) increase CpxP's susceptibility to DegP, leading to CpxP degradation, inducing the Cpx pathway (PubMed:16166523, PubMed:16303867). Aids in combating extracytoplasmic protein-mediated toxicity (PubMed:16303867, PubMed:21239493, PubMed:9473036). Overexpression leads to degradation by DegP of misfolded P pili subunits in the periplasm (tested using PapE) (PubMed:21239493). Inhibits autophosphorylation of CpxA in reconstituted liposomes by 50% but has no effect on phosphatase activity of CpxA (PubMed:17259177, PubMed:21239493). Has mild protein chaperone activity (PubMed:21239493, PubMed:21317898). {ECO:0000269|PubMed:16166523, ECO:0000269|PubMed:16303867, ECO:0000269|PubMed:17259177, ECO:0000269|PubMed:21239493, ECO:0000269|PubMed:21317318, ECO:0000269|PubMed:21317898, ECO:0000269|PubMed:25207645, ECO:0000269|PubMed:9473036}.

## Biological Role

Component of periplasmic protein involved in stress resistence (complex.ecocyc.CPLX0-8155).

## Annotation

FUNCTION: Acts as an auxiliary protein in the Cpx two-component envelope stress response system, helping modulate the Cpx response systems response to some inducers (PubMed:16303867, PubMed:25207645). Binds the periplasmic domain of sensor histidine kinase CpxA, inhibiting induction of the Cpx envelope stress response in the absence of inducer; overexpression decreases Cpx pathway activity (PubMed:16166523, PubMed:21317318). Some periplasmic stimulii (shown for P pili subunit PapE and probably 0.3 M NaCl) increase CpxP's susceptibility to DegP, leading to CpxP degradation, inducing the Cpx pathway (PubMed:16166523, PubMed:16303867). Aids in combating extracytoplasmic protein-mediated toxicity (PubMed:16303867, PubMed:21239493, PubMed:9473036). Overexpression leads to degradation by DegP of misfolded P pili subunits in the periplasm (tested using PapE) (PubMed:21239493). Inhibits autophosphorylation of CpxA in reconstituted liposomes by 50% but has no effect on phosphatase activity of CpxA (PubMed:17259177, PubMed:21239493). Has mild protein chaperone activity (PubMed:21239493, PubMed:21317898). {ECO:0000269|PubMed:16166523, ECO:0000269|PubMed:16303867, ECO:0000269|PubMed:17259177, ECO:0000269|PubMed:21239493, ECO:0000269|PubMed:21317318, ECO:0000269|PubMed:21317898, ECO:0000269|PubMed:25207645, ECO:0000269|PubMed:9473036}.

## Outgoing Edges (1)

- `is_component_of` --> [[complex.ecocyc.CPLX0-8155|complex.ecocyc.CPLX0-8155]] `EcoCyc` `database` - EcoCyc component coefficient=2 | EcoCyc protcplxs.col coefficient=2

## Incoming Edges (1)

- `encodes` <-- [[gene.b4484|gene.b4484]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0AE85`
- `KEGG:ecj:JW5558;eco:b4484;ecoc:C3026_21160;`
- `GeneID:2847688;93778025;`
- `GO:GO:0006950; GO:0030162; GO:0030288; GO:0042802; GO:0051082`

## Notes

Periplasmic protein CpxP (ORF_o167) (Periplasmic accessory protein CpxP)

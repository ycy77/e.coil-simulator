---
entity_id: "protein.P28224"
entity_type: "protein"
name: "mliC"
source_database: "UniProt"
source_id: "P28224"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:18369469}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303, ECO:0000269|PubMed:18369469}. Note=Anchored to the periplasmic side. {ECO:0000269|PubMed:18369469}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mliC ydhA b1639 JW1631"
---

# mliC

`protein.P28224`

## Static

- Type: `protein`
- Source: `UniProt:P28224`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell outer membrane {ECO:0000269|PubMed:18369469}; Lipid-anchor {ECO:0000255|PROSITE-ProRule:PRU00303, ECO:0000269|PubMed:18369469}. Note=Anchored to the periplasmic side. {ECO:0000269|PubMed:18369469}.

## Enriched Summary

FUNCTION: Specifically inhibits C-type lysozymes. {ECO:0000269|PubMed:18369469}. The MliC protein inhibits activity of c-type lysozyme in vitro. In cells that are sensitized to hen egg white lysozyme (HEWL), overexpression of MliC suppresses growth inhibition by HEWL. MliC is predicted to be a lipoprotein that is anchored to the periplasmic side of the outer membrane; activity is found in the membrane fraction . A solution structure of MliC has been determined, showing an eight-stranded β-barrel . An mliC (ORF1) insertion mutation has no detectable phenotype, and no expression was detected in exponentially growing cells . Overexpression of mliC suppresses the essentiality of EG12691-MONOMER "lapB", which encodes a protein involved in lipopolysaccharide (LPS) assembly . MliC: "membrane-bound lysozyme inhibitor of c-type lysozyme"

## Annotation

FUNCTION: Specifically inhibits C-type lysozymes. {ECO:0000269|PubMed:18369469}.

## Outgoing Edges (0)

_None._

## Incoming Edges (1)

- `encodes` <-- [[gene.b1639|gene.b1639]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P28224`
- `KEGG:ecj:JW1631;eco:b1639;ecoc:C3026_09415;`
- `GeneID:946811;`
- `GO:GO:0009279; GO:0060241`

## Notes

Membrane-bound lysozyme inhibitor of C-type lysozyme

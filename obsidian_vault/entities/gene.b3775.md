---
entity_id: "gene.b3775"
entity_type: "gene"
name: "ppiC"
source_database: "NCBI RefSeq"
source_id: "gene-b3775"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3775"
  - "ppiC"
---

# ppiC

`gene.b3775`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3775`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ppiC (gene.b3775) is a gene entity. It encodes ppiC (protein.P0A9L5). Encoded protein function: FUNCTION: PPIases accelerate the folding of proteins (Probable). It prefers amino acid residues with hydrophobic side chains like leucine and phenylalanine in the P1 position of the peptides substrates. {ECO:0000305}. EcoCyc product frame: EG12352-MONOMER. EcoCyc synonyms: parvA. Genomic coordinates: 3959532-3959813. EcoCyc protein note: ppiC encodes a peptidyl-prolyl cis-trans isomerase (PPIase), parvulin, which defines a new family of PPIases . Unlike other PPIases, the enzymatic activity of parvulin is not inhibited by FK506 or cyclosporin A . The natural compound juglone specifically and irreversibly inactivates parvulin by covalent modification . EG11384-MONOMER AhpC has been identified as a specific interaction partner of PpiC . Additional substrates were identified by pull-down assays and co-IP . The stereospecificity of the enzyme has been studied , and a solution structure of PpiC has been determined . Mutants in predicted active site residues were assayed for potential substrate binding and PPIase activity . A ppiC mutant is more sensitive to oxidative stress than wild type . A strain containing non-polar deletions of all six cytoplasmic PPIases (Δ6ppi) shows a growth defect at 37°C in rich media and at 43°C in both rich and minimal media...

## Biological Role

Repressed by yidZ (protein.P31463).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9L5|protein.P0A9L5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `represses` <-- [[protein.P31463|protein.P31463]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012334,ECOCYC:EG12352,GeneID:948285`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3959532-3959813:-; feature_type=gene

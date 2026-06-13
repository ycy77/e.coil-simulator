---
entity_id: "gene.b2169"
entity_type: "gene"
name: "fruB"
source_database: "NCBI RefSeq"
source_id: "gene-b2169"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2169"
  - "fruB"
---

# fruB

`gene.b2169`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2169`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

fruB (gene.b2169) is a gene entity. It encodes fruB (protein.P69811). Encoded protein function: FUNCTION: The phosphoenolpyruvate-dependent sugar phosphotransferase system (sugar PTS), a major carbohydrate active transport system, catalyzes the phosphorylation of incoming sugar substrates concomitantly with their translocation across the cell membrane. The enzyme II FruAB PTS system is involved in fructose transport. {ECO:0000269|PubMed:3510127, ECO:0000305|PubMed:8013873}. EcoCyc product frame: MONOMER0-4306. EcoCyc synonyms: fpr, fruF. Genomic coordinates: 2262365-2263495. EcoCyc protein note: fruB encodes a tridomain protein in which a IIA domain is linked to an HPr-like domain called FPr (fructose-inducible HPr) or H by a central domain (M) of unknown function . Phosphate transfer to fructose by the fructose PTS occurs via the FPr domain of FruB rather than by HPr as is typical for other PTS pathways . Phosphate transfer is predicted to occur from Enzyme I (PtsI) to histidine residue 299 in the FruB H domain to histidine residue 62 in the FruB IIA domain. FruB is also known as the diphosphoryl transfer protein (DTP). EcoCyc protein note: A modified form of FruB phosphorylated at histidine residue 299

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930).

## Enriched Pathways

- `eco02060` Phosphotransferase system (PTS) (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69811|protein.P69811]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `S` - regulator=Cra; target=fruB; function=-

## External IDs

- `Dbxref:ASAP:ABE-0007180,ECOCYC:G7990,GeneID:946677`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2262365-2263495:-; feature_type=gene

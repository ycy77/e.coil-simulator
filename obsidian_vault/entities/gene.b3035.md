---
entity_id: "gene.b3035"
entity_type: "gene"
name: "tolC"
source_database: "NCBI RefSeq"
source_id: "gene-b3035"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3035"
  - "tolC"
---

# tolC

`gene.b3035`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3035`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tolC (gene.b3035) is a gene entity. It encodes tolC (protein.P02930). Encoded protein function: FUNCTION: Outer membrane channel, which is required for the function of several efflux systems such as AcrAB-TolC, AcrEF-TolC, EmrAB-TolC and MacAB-TolC (PubMed:11274125, PubMed:15228545, PubMed:18955484, PubMed:28355133, PubMed:28504659, PubMed:31201302, PubMed:40083904, PubMed:40461577, PubMed:6337123). These systems are involved in export of antibiotics and other toxic compounds from the cell (PubMed:11274125, PubMed:18955484, PubMed:28504659). As part of the system, involved in the efflux of the immediate heme precursor, protoporphyrin IX (PPIX), which is probably an endogenous substrate (PubMed:25257218). Plays a role in substrate specificity during efflux (PubMed:32850959). TolC is also involved in import of colicin E1 into the cells (PubMed:23176499, PubMed:35199644). {ECO:0000269|PubMed:11274125, ECO:0000269|PubMed:15228545, ECO:0000269|PubMed:18955484, ECO:0000269|PubMed:23176499, ECO:0000269|PubMed:25257218, ECO:0000269|PubMed:28355133, ECO:0000269|PubMed:28504659, ECO:0000269|PubMed:31201302, ECO:0000269|PubMed:32850959, ECO:0000269|PubMed:35199644, ECO:0000269|PubMed:40083904, ECO:0000269|PubMed:40461577, ECO:0000269|PubMed:6337123}. EcoCyc product frame: EG11009-MONOMER. EcoCyc synonyms: weeA, colE1-i, mtcB, mukA, refI, toc. Genomic coordinates: 3178115-3179596.

## Biological Role

Repressed by sdsR (gene.b4433). Activated by DNA-binding transcriptional dual regulator OmpR-phosphorylated (complex.ecocyc.PHOSPHO-OMPR), ompR (protein.P0AA16), rpoS (protein.P13445).

## Enriched Pathways

- `eco01501` beta-Lactam resistance (KEGG)
- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)
- `eco02020` Two-component system (KEGG)
- `eco03070` Bacterial secretion system (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P02930|protein.P02930]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[complex.ecocyc.PHOSPHO-OMPR|complex.ecocyc.PHOSPHO-OMPR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0AA16|protein.P0AA16]] `RegulonDB` `S` - regulator=OmpR; target=tolC; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=tolC; function=+
- `represses` <-- [[gene.b4433|gene.b4433]] `RegulonDB` `S` - regulator=SdsR; target=tolC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0009965,ECOCYC:EG11009,GeneID:947521`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3178115-3179596:+; feature_type=gene

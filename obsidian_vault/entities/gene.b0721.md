---
entity_id: "gene.b0721"
entity_type: "gene"
name: "sdhC"
source_database: "NCBI RefSeq"
source_id: "gene-b0721"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0721"
  - "sdhC"
---

# sdhC

`gene.b0721`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0721`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

sdhC (gene.b0721) is a gene entity. It encodes sdhC (protein.P69054). Encoded protein function: FUNCTION: Membrane-anchoring subunit of succinate dehydrogenase (SDH). EcoCyc product frame: SDH-MEMB1. EcoCyc synonyms: cybL, cybA, dhsC. Genomic coordinates: 755177-755566. EcoCyc protein note: SdhC is one of two membrane proteins in the four subunit succinate dehydrogenase (SQR) enzyme. SdhC and SdhD are the large and small subunits of cytochrome b556, respectively . The quinone binding (Qp) site resides in the interface between SdhB, SdhC and SdhD . The b556 type heme bridges both membrane subunits . Mutation of key heme binding residues in SdhC and SdhD does not affect proper assembly or physiological function of the complex . Despite similar function, hydrophobicity, and protein size, the SdhC and SdhD subunits of succinate dehydrogenase do not share significant sequence identity with the corresponding membrane-binding subunits of fumarate reductase, FrdC and FrdD .

## Biological Role

Repressed by DNA-binding transcriptional dual regulator CpxR-phosphorylated (complex.ecocyc.CPLX0-7748), rybB (gene.b4417), fur (protein.P0A9A9), arcA (protein.P0A9Q1). Activated by rpoD (protein.P00579), fur (protein.P0A9A9), arcA (protein.P0A9Q1), crp (protein.P0ACJ8), nac (protein.Q47005).

## Enriched Pathways

- `eco00020` Citrate cycle (TCA cycle) (KEGG)
- `eco00190` Oxidative phosphorylation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco00720` Other carbon fixation pathways (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01200` Carbon metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69054|protein.P69054]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=sdhC; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sdhC; function=-+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sdhC; function=-+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=sdhC; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[complex.ecocyc.CPLX0-7748|complex.ecocyc.CPLX0-7748]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[gene.b4417|gene.b4417]] `RegulonDB` `S` - regulator=RybB; target=sdhC; function=-
- `represses` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=sdhC; function=-+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=sdhC; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0002460,ECOCYC:EG10933,GeneID:945316`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:755177-755566:+; feature_type=gene

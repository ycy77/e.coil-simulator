---
entity_id: "gene.b3806"
entity_type: "gene"
name: "cyaA"
source_database: "NCBI RefSeq"
source_id: "gene-b3806"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3806"
  - "cyaA"
---

# cyaA

`gene.b3806`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3806`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

cyaA (gene.b3806) is a gene entity. It encodes cyaA (protein.P00936). Encoded protein function: FUNCTION: Catalyzes the formation of the second messenger cAMP from ATP. Its transcript is probably degraded by endoribonuclease LS (rnlA), decreasing cAMP levels and the negative regulator Crp-cAMP, which then induces its own transcription again. EcoCyc product frame: ADENYLATECYC-MONOMER. EcoCyc synonyms: cya. Genomic coordinates: 3991153-3993699. EcoCyc protein note: Adenylate cyclase catalyzes the synthesis of cyclic AMP (cAMP) by an intramolecular transfer of the adenylyl group of ATP to the 3'-hydroxy group, releasing pyrophosphate; thus, CyaA helps regulate the cellular concentration of cAMP. cAMP is an important signaling molecule; the role of cAMP in regulating the production of metabolic enzymes was first summarized in . The absence of cAMP affects the expression of alternative carbon source uptake and degradation systems involved in central metabolism . Via binding to the CAP/CRP protein (see CPLX0-226), it participates in the regulation of transcription of many genes. Adenylate cyclase is present at very low levels of approximately 15 molecules/cell . Its rare UUG initiation codon, which was confirmed by N-terminal sequencing of the purified protein , limits the translation of cyaA...

## Biological Role

Repressed by crp (protein.P0ACJ8). Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00230` Purine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco02026` Biofilm formation - Escherichia coli (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P00936|protein.P00936]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=cyaA; function=+
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=cyaA; function=-

## External IDs

- `Dbxref:ASAP:ABE-0012432,ECOCYC:EG10170,GeneID:947755`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3991153-3993699:+; feature_type=gene

---
entity_id: "gene.b0417"
entity_type: "gene"
name: "thiL"
source_database: "NCBI RefSeq"
source_id: "gene-b0417"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0417"
  - "thiL"
---

# thiL

`gene.b0417`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0417`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

thiL (gene.b0417) is a gene entity. It encodes thiL (protein.P0AGG0). Encoded protein function: FUNCTION: Catalyzes the ATP-dependent phosphorylation of thiamine-monophosphate (TMP) to form thiamine-pyrophosphate (TPP), the active form of vitamin B1. Cannot use thiamine as substrate. Is highly specific for ATP as phosphate donor. {ECO:0000269|PubMed:4567662, ECO:0000269|PubMed:6284709}. EcoCyc product frame: THI-P-KIN-MONOMER. EcoCyc synonyms: thiJ. Genomic coordinates: 435634-436611. EcoCyc protein note: Thiamine phosphate kinase (ThiL) is involved in the final step of thiamine biosynthesis. ThiL catalyzes the phosphorylation of thiamine monophosphate to yield thiamine diphosphate in the presence of ATP and Mg2+ . Mutations in thiL resulted in a requirement for thiamine pyrophosphate for growth . In Salmonella typhimurium, altered ThiL activity resulted in decreased repression of transcription of thiamine pyrophosphate-regulated genes . The ThiL structure with substrate and product complexes in Aquifex aeolicus was determined .

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoH (protein.P0AGB3).

## Enriched Pathways

- `eco00730` Thiamine metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AGG0|protein.P0AGG0]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0AGB3|protein.P0AGB3]] `RegulonDB` `S` - sigma=sigma32; target=thiL; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=thiL; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0001452,ECOCYC:G6234,GeneID:947387`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:435634-436611:+; feature_type=gene

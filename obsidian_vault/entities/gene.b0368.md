---
entity_id: "gene.b0368"
entity_type: "gene"
name: "tauD"
source_database: "NCBI RefSeq"
source_id: "gene-b0368"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0368"
  - "tauD"
---

# tauD

`gene.b0368`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0368`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tauD (gene.b0368) is a gene entity. It encodes tauD (protein.P37610). Encoded protein function: FUNCTION: Catalyzes the alpha-ketoglutarate-dependent hydroxylation of taurine yielding sulfite and aminoacetaldehyde after decomposition of an unstable intermediate (PubMed:9287300). Is required for the utilization of taurine (2-aminoethanesulfonate) as an alternative sulfur source for growth in the absence of sulfate (PubMed:8808933). To a lesser extent, pentanesulfonate, 3-(N-morpholino)propanesulfonate and 1,3-dioxo-2-isoindolineethanesulfonate are also desulfonated by this enzyme in vitro; however, desulfonation by TauD of organosulfonates other than taurine seem to be of little or no importance for sulfur metabolism in vivo (PubMed:9287300). {ECO:0000269|PubMed:8808933, ECO:0000269|PubMed:9287300}. EcoCyc product frame: MONOMER0-147. EcoCyc synonyms: ssiD, yaiG. Genomic coordinates: 387795-388646.

## Biological Role

Activated by cysB (protein.P0A9F3), cbl (protein.Q47083).

## Enriched Pathways

- `eco00430` Taurine and hypotaurine metabolism (KEGG)
- `eco00920` Sulfur metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37610|protein.P37610]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P0A9F3|protein.P0A9F3]] `RegulonDB` `S` - regulator=CysB; target=tauD; function=+
- `activates` <-- [[protein.Q47083|protein.Q47083]] `RegulonDB` `S` - regulator=Cbl; target=tauD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0001263,ECOCYC:EG12423,GeneID:945021`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:387795-388646:+; feature_type=gene

---
entity_id: "gene.b1132"
entity_type: "gene"
name: "hflD"
source_database: "NCBI RefSeq"
source_id: "gene-b1132"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1132"
  - "hflD"
---

# hflD

`gene.b1132`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1132`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hflD (gene.b1132) is a gene entity. It encodes hflD (protein.P25746). Encoded protein function: FUNCTION: Negative regulator of phage lambda lysogenization. Contributes to the degradation of the phage regulatory protein CII. Acts probably by holding CII on the membrane surface, away from the target promoters, but close to the FtsH protease. {ECO:0000269|PubMed:11278968}. EcoCyc product frame: EG11345-MONOMER. EcoCyc synonyms: hslZ, ycfC. Genomic coordinates: 1191990-1192631. EcoCyc protein note: hflD encodes an inner membrane-associated protein that directly interacts with protein CII of bacteriophage λ, making it more vulnerable to proteolysis by FtsH and inhibiting DNA binding of CII , thus leading to decreased lysogenization frequency of λ . What role HflD may have in the uninfected host is as yet unknown . An hflD mutant shows increased λ CII-dependent transcription, and thus an increased frequency of lysogenization . The Keio collection hflD mutant exhibits a 'low level' of resistance to lithium exposure . HflD: "high frequency lysogenization"

## Biological Role

Repressed by purR (protein.P0ACP7). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P25746|protein.P25746]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hflD; function=+
- `represses` <-- [[protein.P0ACP7|protein.P0ACP7]] `RegulonDB` `S` - regulator=PurR; target=hflD; function=-

## External IDs

- `Dbxref:ASAP:ABE-0003812,ECOCYC:EG11345,GeneID:945693`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1191990-1192631:-; feature_type=gene

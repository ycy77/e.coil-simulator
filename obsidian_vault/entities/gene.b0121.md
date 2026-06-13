---
entity_id: "gene.b0121"
entity_type: "gene"
name: "speE"
source_database: "NCBI RefSeq"
source_id: "gene-b0121"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0121"
  - "speE"
---

# speE

`gene.b0121`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0121`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

speE (gene.b0121) is a gene entity. It encodes speE (protein.P09158). Encoded protein function: FUNCTION: Involved in the biosynthesis of polyamines which play a significant role in the structural and functional organization in the chromoid of E.coli by compacting DNA and neutralizing negative charges. Catalyzes the irreversible transfer (ping-pong mechanism) of a propylamine group from the amino donor S-adenosylmethioninamine (decarboxy-AdoMet) to putrescine (1,4-diaminobutane) to yield spermidine. Cadaverine (1,5-diaminopentane) and spermidine can also be used as the propylamine acceptor. {ECO:0000269|PubMed:23001854, ECO:0000269|PubMed:4572733}. EcoCyc product frame: SPERMIDINESYN-MONOMER. Genomic coordinates: 135598-136464.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00270` Cysteine and methionine metabolism (KEGG)
- `eco00330` Arginine and proline metabolism (KEGG)
- `eco00480` Glutathione metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P09158|protein.P09158]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=speE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000418,ECOCYC:EG10963,GeneID:947726`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:135598-136464:-; feature_type=gene

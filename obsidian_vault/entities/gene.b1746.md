---
entity_id: "gene.b1746"
entity_type: "gene"
name: "astD"
source_database: "NCBI RefSeq"
source_id: "gene-b1746"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1746"
  - "astD"
---

# astD

`gene.b1746`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1746`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

astD (gene.b1746) is a gene entity. It encodes astD (protein.P76217). Encoded protein function: FUNCTION: Catalyzes the NAD-dependent reduction of succinylglutamate semialdehyde into succinylglutamate (Probable). Also shows in vitro activity with decanal or succinic semialdehyde as the electron donor and NAD as the electron acceptor. No activity is detected with NADP as the electron acceptor. Therefore, is an aldehyde dehydrogenase with broad substrate specificity (PubMed:15808744). {ECO:0000269|PubMed:15808744, ECO:0000305|PubMed:9696779}. EcoCyc product frame: SUCCGLUALDDEHYD-MONOMER. EcoCyc synonyms: ydjU. Genomic coordinates: 1828256-1829734. EcoCyc protein note: Succinylglutamate semialdehyde dehydrogenase catalyzes the fourth reaction in the ammonia-producing arginine catabolic pathway, AST-PWY. The activity has only been assayed in crude cell extracts, and thus there is little direct evidence for the function of the astD gene product . However, a high-throughput screen of purified proteins showed that AstD is an aldehyde dehydrogenase with broad substrate specificity. The enzyme is active with NAD, but not NADP, as the electron acceptor . Expression of the enzymes of the AST pathway is regulated by arginine and nitrogen availability via ArgR and NtrC . astD was identified in a screen for genes that are activated by conditioned medium...

## Biological Role

Activated by argR (protein.P0A6D0), glnG (protein.P0AFB8), rpoS (protein.P13445), rpoN (protein.P24255).

## Enriched Pathways

- `eco00330` Arginine and proline metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76217|protein.P76217]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P0A6D0|protein.P0A6D0]] `RegulonDB` `S` - regulator=ArgR; target=astD; function=+
- `activates` <-- [[protein.P0AFB8|protein.P0AFB8]] `RegulonDB` `S` - regulator=NtrC; target=astD; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `C` - sigma=sigma38; target=astD; function=+
- `activates` <-- [[protein.P24255|protein.P24255]] `RegulonDB` `C` - sigma=sigma54; target=astD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0005820,ECOCYC:G6942,GeneID:946260`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1828256-1829734:-; feature_type=gene

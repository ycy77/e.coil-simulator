---
entity_id: "gene.b3605"
entity_type: "gene"
name: "lldD"
source_database: "NCBI RefSeq"
source_id: "gene-b3605"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3605"
  - "lldD"
---

# lldD

`gene.b3605`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3605`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

lldD (gene.b3605) is a gene entity. It encodes lldD (protein.P33232). Encoded protein function: FUNCTION: Catalyzes the conversion of L-lactate to pyruvate. Seems to be a primary dehydrogenase in the respiratory chain. To a lesser extent, can also oxidize DL-alpha-hydroxybutyrate, but not D-lactate. {ECO:0000269|PubMed:18473, ECO:0000269|PubMed:8407843}. EcoCyc product frame: L-LACTDEHYDROGFMN-MONOMER. EcoCyc synonyms: lct, lctD. Genomic coordinates: 3779827-3781017. EcoCyc protein note: L-lactate dehydrogenase is an FMN-dependent membrane-associated dehydrogenase . It functions in aerobic respiration and also has a role in anaerobic nitrate respiration . L-lactate dehydrogenase is associated with the inner membrane . LldD is one of three lactate dehydrogenase enzymes which interconvert pyruvate and lactate in E. coli. The other two enzymes are specific for D-lactate: the soluble DLACTDEHYDROGNAD-MONOMER "LdhA", an NAD-linked fermentative enzyme, and DLACTDEHYDROGFAD-MONOMER "Dld", a membrane-associated respiratory enzyme. L-lactate dehydrogenase is induced by aerobic growth on L-lactate and L-fucose and in the presence of lactate under nitrate, fumarate and TMAO respiration conditions . Repression of lldD expression under anaerobic conditions is mediated by ArcA...

## Biological Role

Repressed by arcA (protein.P0A9Q1), lldR (protein.P0ACL7). Activated by rpoD (protein.P00579), lldR (protein.P0ACL7).

## Enriched Pathways

- `eco00620` Pyruvate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33232|protein.P33232]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=lldD; function=+
- `activates` <-- [[protein.P0ACL7|protein.P0ACL7]] `RegulonDB` `C` - regulator=LldR; target=lldD; function=-+
- `represses` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `C` - regulator=ArcA; target=lldD; function=-
- `represses` <-- [[protein.P0ACL7|protein.P0ACL7]] `RegulonDB` `C` - regulator=LldR; target=lldD; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011784,ECOCYC:EG11963,GeneID:948121`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3779827-3781017:+; feature_type=gene

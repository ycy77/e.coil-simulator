---
entity_id: "gene.b3733"
entity_type: "gene"
name: "atpG"
source_database: "NCBI RefSeq"
source_id: "gene-b3733"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3733"
  - "atpG"
---

# atpG

`gene.b3733`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3733`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

atpG (gene.b3733) is a gene entity. It encodes atpG (protein.P0ABA6). Encoded protein function: FUNCTION: Produces ATP from ADP in the presence of a proton gradient across the membrane. The gamma chain is believed to be important in regulating ATPase activity and the flow of protons through the CF(0) complex. EcoCyc product frame: ATPG-MONOMER. EcoCyc synonyms: papC, uncG. Genomic coordinates: 3917402-3918265. EcoCyc protein note: The gamma subunit appears to play an important role in coupling the catalytic site events with proton translocation in association with the epsilon subunit. The coupling involves conformational changes and probable translocations of one or both subunits . The rate limiting rotation step carried out by this subunit has been investigated and residues involved in this rotation process have been identified . ArcA appears to repress atpG gene expression under anaerobiosis. Two putative ArcA binding sites were identified upstream of this gene , but no promoter upstream of it has been identified. Instead, atpG is transcribed from three promoters: one of them is located usptream of atpI gene and the others are located upstream of atpB gene.

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00190` Oxidative phosphorylation (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABA6|protein.P0ABA6]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=atpG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0012211,ECOCYC:EG10104,GeneID:948243`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3917402-3918265:-; feature_type=gene

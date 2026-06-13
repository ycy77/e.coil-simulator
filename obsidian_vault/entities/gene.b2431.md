---
entity_id: "gene.b2431"
entity_type: "gene"
name: "yfeX"
source_database: "NCBI RefSeq"
source_id: "gene-b2431"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2431"
  - "yfeX"
---

# yfeX

`gene.b2431`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2431`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yfeX (gene.b2431) is a gene entity. It encodes yfeX (protein.P76536). Encoded protein function: FUNCTION: Has both general peroxidase activity and dye-decolorizing activity. Can catalyze the oxidation of both protoporphyrinogen IX and coproporphyrinogen III to their corresponding porphyrins. Also efficiently decolorizes the dyes alizarin red and Cibacron blue F3GA. {ECO:0000269|PubMed:22068980}. EcoCyc product frame: G7266-MONOMER. Genomic coordinates: 2549646-2550545. EcoCyc protein note: YfeX belongs to the family of dye-decolorizing (DyP-type) peroxidases and is able to oxidize both protoporphyrinogen IX and coproporphyrinogen III to their corresponding porphyrins . A crystal structure of heme-bound YfeX from E. coli O157:H7 str. Sakai has been solved at 2.09 Å resolution. Site-directed mutagenesis of the predicted active site residues D143 And R232 indicate that their importance for catalysis is dependent on the substrate . The sequences of the E. coli O157:H7 str. Sakai and K-12 MG1655 proteins are 99% identical. Additional mutants in predicted active site residues were tested for heme binding ability . The authors of were unable to reproduce dechelation of iron from protoheme or mesoheme, disputing the results of , described below: Due to the lack of an outer membrane receptor for heme, E. coli K-12 is unable to utilize heme as a source of iron...

## Biological Role

Activated by rpoE (protein.P0AGB6).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76536|protein.P76536]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P0AGB6|protein.P0AGB6]] `RegulonDB` `S` - sigma=sigma24; target=yfeX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0008015,ECOCYC:G7266,GeneID:946913`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2549646-2550545:-; feature_type=gene

---
entity_id: "gene.b3431"
entity_type: "gene"
name: "glgX"
source_database: "NCBI RefSeq"
source_id: "gene-b3431"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3431"
  - "glgX"
---

# glgX

`gene.b3431`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3431`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

glgX (gene.b3431) is a gene entity. It encodes glgX (protein.P15067). Encoded protein function: FUNCTION: Removes maltotriose and maltotetraose chains that are attached by 1,6-alpha-linkage to the limit dextrin main chain, generating a debranched limit dextrin. Shows only very little activity with native glycogen. {ECO:0000269|PubMed:15687211, ECO:0000269|PubMed:779849, ECO:0000269|PubMed:8576033}. EcoCyc product frame: EG10381-MONOMER. Genomic coordinates: 3569346-3571319. EcoCyc protein note: GlgX is a glycogen debranching enzyme. The purified enzyme shows only low activity toward Glycogens glycogen itself, but hydrolyzes 1,6-α-glucosidic linkages in CPD0-971 "limit dextrins" prepared from glycogen and amylopectin by treatment with phosphorylase and β-amylase . Recombinant GlgX efficiently hydrolyzes α-1,6-glucosidic linkages with degrees of polymerization of three or four glucose residues, and has very low or no activity with longer chains . The crystal structure of the enzyme has been determined at 2.25 Å resolution. The enzyme was found to be a monomer consisting of three major domains. A structural feature at the substrate binding groove suggests the basis of its unique specificity for G4 phosphorylase-limit dextrin and its discrimination toward substrates of varying length...

## Biological Role

Activated by rpoD (protein.P00579).

## Enriched Pathways

- `eco00500` Starch and sucrose metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P15067|protein.P15067]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=glgX; function=+

## External IDs

- `Dbxref:ASAP:ABE-0011206,ECOCYC:EG10381,GeneID:947941`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3569346-3571319:-; feature_type=gene

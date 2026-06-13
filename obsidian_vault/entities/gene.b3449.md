---
entity_id: "gene.b3449"
entity_type: "gene"
name: "ugpQ"
source_database: "NCBI RefSeq"
source_id: "gene-b3449"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3449"
  - "ugpQ"
---

# ugpQ

`gene.b3449`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3449`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ugpQ (gene.b3449) is a gene entity. It encodes ugpQ (protein.P10908). Encoded protein function: FUNCTION: Glycerophosphodiester phosphodiesterase hydrolyzes glycerophosphodiesters into glycerol-3-phosphate (G3P) and the corresponding alcohol. {ECO:0000269|PubMed:18083802}. EcoCyc product frame: GLYCPDIESTER-CYTO-MONOMER. Genomic coordinates: 3587370-3588113. EcoCyc protein note: UgpQ is a cytosolic glycerophosphodiester phosphodiesterase with broad substrate specificity . Initial experiments suggested that cytoplasmic glycerophosphodiesters are not substrates of UgpQ, and that they are hydrolyzed only when transported by the Ugp system . However, recent purification and characterization of the enzyme contradicts those results . Moreover, purified UgpQ does not affect the activity of the UgpB-EAC2 transporter complex in vitro . Expression of UgpQ is induced by phosphate starvation . The ugp operon is induced by carbon starvation during the late logarithmic growth phase . UgpQ: "uptake of glycerol phosphate"

## Biological Role

Repressed by phoB (protein.P0AFJ5). Activated by rpoD (protein.P00579), crp (protein.P0ACJ8), phoB (protein.P0AFJ5).

## Enriched Pathways

- `eco00564` Glycerophospholipid metabolism (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P10908|protein.P10908]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ugpQ; function=+
- `activates` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=ugpQ; function=+
- `activates` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=ugpQ; function=-+
- `represses` <-- [[protein.P0AFJ5|protein.P0AFJ5]] `RegulonDB` `S` - regulator=PhoB; target=ugpQ; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011264,ECOCYC:EG11050,GeneID:947955`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3587370-3588113:-; feature_type=gene

---
entity_id: "gene.b3038"
entity_type: "gene"
name: "ygiC"
source_database: "NCBI RefSeq"
source_id: "gene-b3038"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3038"
  - "ygiC"
---

# ygiC

`gene.b3038`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3038`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ygiC (gene.b3038) is a gene entity. It encodes ygiC (protein.P0ADT5). Encoded protein function: FUNCTION: May be a ligase forming an amide bond. Shows ATPase activity. Despite its similarity to the C-terminal synthetase domain of Gss, is not a glutathionylspermidine (Gsp) synthetase. Cannot synthesize Gsp, glutathione (GSH), or GSH intermediates, from GSH and spermidine, cysteine and glutamate, gamma-glutamylcysteine and spermidine, and gamma-glutamylcysteine and glycine. Does not bind to Gsp. {ECO:0000269|PubMed:23097746}. EcoCyc product frame: EG11165-MONOMER. Genomic coordinates: 3180421-3181581. EcoCyc protein note: Based on sequence similarity to the glutathionylspermidine synthetase domain of GSP-CPLX "Gss", EG11165 and EG11812 were predicted to encode additional glutathionylspermidine synthetases. However, while purified YgiC hydrolyzes ATP, it does not synthesize glutathionylspermidine, glutathione, or glutathione intermediates . In addition, a triple mutant lacking EG12882, EG11165 and EG11812 has no growth defect in minimal medium , and deletion of EG11812 has no effect on GLUTATHIONYLSPERMIDINE levels in the cell...

## Biological Role

Activated by rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ADT5|protein.P0ADT5]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=ygiC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009971,ECOCYC:EG11165,GeneID:947249`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3180421-3181581:+; feature_type=gene

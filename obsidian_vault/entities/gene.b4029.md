---
entity_id: "gene.b4029"
entity_type: "gene"
name: "yjbH"
source_database: "NCBI RefSeq"
source_id: "gene-b4029"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4029"
  - "yjbH"
---

# yjbH

`gene.b4029`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4029`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjbH (gene.b4029) is a gene entity. It encodes yjbH (protein.P32689). Encoded protein function: Uncharacterized lipoprotein YjbH EcoCyc product frame: EG11926-MONOMER. Genomic coordinates: 4237634-4239730. EcoCyc protein note: The yjbEFGH operon is involved in the production of an extracellular polysaccharide . Sequence similarity suggests that YjbH may be a lipoprotein and/or an outer membrane porin . Overexpression of yjbEFGH alters colony morphology and leads to increased binding of toluidine blue-O and Congo red, indicating increased production of an EPS that is distinct from colanic acid . Disruption of yjbE has a polar effect on expression of yjbFGH, indicating that these genes form an operon; however, a full-length mRNA could not be detected, possibly due to strong secondary structure in the yjbE-yjbF intergenic region . Expression of yjbEFGH is highest at slow growth rates, low cell density and high oxygen availability; expression is higher in an rpoS mutant and induced by 0.7 M NaCl .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32689|protein.P32689]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yjbH; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013176,ECOCYC:EG11926,GeneID:948527`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4237634-4239730:+; feature_type=gene

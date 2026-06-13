---
entity_id: "gene.b4027"
entity_type: "gene"
name: "yjbF"
source_database: "NCBI RefSeq"
source_id: "gene-b4027"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4027"
  - "yjbF"
---

# yjbF

`gene.b4027`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4027`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjbF (gene.b4027) is a gene entity. It encodes yjbF (protein.P32687). Encoded protein function: Uncharacterized lipoprotein YjbF EcoCyc product frame: EG11924-MONOMER. Genomic coordinates: 4236262-4236900. EcoCyc protein note: The yjbEFGH operon is involved in the production of an extracellular polysaccharide . Sequence similarity suggests that YjbF may be a lipoprotein and/or an outer membrane porin . YjbF is a verified lipoprotein according to unpublished data by S. Matsuyama et al. (cited in ). Overexpression of yjbEFGH alters colony morphology and leads to increased binding of toluidine blue-O and Congo red, indicating increased production of an EPS that is distinct from colanic acid . Expression of yjbF is positively regulated by RcsC . Disruption of yjbE has a polar effect on expression of yjbFGH, indicating that these genes form an operon; however, a full-length mRNA could not be detected, possibly due to strong secondary structure in the yjbE-yjbF intergenic region . Expression of yjbEFGH is highest at slow growth rates, low cell density and high oxygen availability; expression is higher in an rpoS mutant and induced by 0.7 M NaCl .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32687|protein.P32687]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yjbF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013172,ECOCYC:EG11924,GeneID:948533`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4236262-4236900:+; feature_type=gene

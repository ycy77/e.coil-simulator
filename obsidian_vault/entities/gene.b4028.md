---
entity_id: "gene.b4028"
entity_type: "gene"
name: "yjbG"
source_database: "NCBI RefSeq"
source_id: "gene-b4028"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4028"
  - "yjbG"
---

# yjbG

`gene.b4028`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4028`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjbG (gene.b4028) is a gene entity. It encodes yjbG (protein.P32688). Encoded protein function: Uncharacterized protein YjbG EcoCyc product frame: EG11925-MONOMER. Genomic coordinates: 4236897-4237634. EcoCyc protein note: The yjbEFGH operon is involved in the production of an extracellular polysaccharide . Overexpression of yjbEFGH alters colony morphology and leads to increased binding of toluidine blue-O and Congo red, indicating increased production of an EPS that is distinct from colanic acid . Expression of yjbG is positively regulated by RcsC . Disruption of yjbE has a polar effect on expression of yjbFGH, indicating that these genes form an operon; however, a full-length mRNA could not be detected, possibly due to strong secondary structure in the yjbE-yjbF intergenic region . Expression of yjbEFGH is highest at slow growth rates, low cell density and high oxygen availability; expression is higher in an rpoS mutant and induced by 0.7 M NaCl . A ΔyjbG rpoS::Tn10 mutant does not show extreme mucoidy on LB plates, but does produce increased amounts of extracellular polysaccharides as measured by a pelleting assay .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P32688|protein.P32688]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yjbG; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013174,ECOCYC:EG11925,GeneID:948526`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4236897-4237634:+; feature_type=gene

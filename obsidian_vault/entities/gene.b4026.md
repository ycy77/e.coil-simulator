---
entity_id: "gene.b4026"
entity_type: "gene"
name: "yjbE"
source_database: "NCBI RefSeq"
source_id: "gene-b4026"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b4026"
  - "yjbE"
---

# yjbE

`gene.b4026`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b4026`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

yjbE (gene.b4026) is a gene entity. It encodes yjbE (protein.P0AF45). Encoded protein function: Uncharacterized protein YjbE EcoCyc product frame: EG11923-MONOMER. Genomic coordinates: 4235906-4236148. EcoCyc protein note: The yjbEFGH operon is involved in the production of an extracellular polysaccharide . Published reports disagree on whether YjbE is involved in biofilm formation. A mutant with a deletion of yjbE showed a significant decrease in biofilm formation . However, other experiments showed that a yjbE mutant had no effect on biofilm formation . Overexpression of yjbEFGH altered colony morphology and led to increased binding of toluidine blue-O and Congo red, indicating increased production of an EPS that is distinct from colanic acid . Expression of yjbE is positively regulated by RcsC and increases 7.5-fold upon deletion of tqsA, which increases biofilm formation . Disruption of yjbE has a polar effect on expression of yjbFGH, indicating that these genes form an operon; however, a full-length mRNA could not be detected, possibly due to strong secondary structure in the yjbE-yjbF intergenic region . Expression of yjbEFGH is highest at slow growth rates, low cell density and high oxygen availability; expression is higher in an rpoS mutant and induced by 0.7 M NaCl . A ΔyjbE rpoS::Tn10 double mutant shows extreme mucoidy and a filamentous phenotype .

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AF45|protein.P0AF45]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=yjbE; function=+

## External IDs

- `Dbxref:ASAP:ABE-0013168,ECOCYC:EG11923,GeneID:948534`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4235906-4236148:+; feature_type=gene

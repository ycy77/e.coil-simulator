---
entity_id: "gene.b2991"
entity_type: "gene"
name: "hybF"
source_database: "NCBI RefSeq"
source_id: "gene-b2991"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2991"
  - "hybF"
---

# hybF

`gene.b2991`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2991`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hybF (gene.b2991) is a gene entity. It encodes hybF (protein.P0A703). Encoded protein function: FUNCTION: Involved in the maturation of [NiFe] hydrogenases. Required for nickel insertion into the metal center of the hydrogenase. HybF is involved in maturation of hydrogenases 1 and 2. It may partially substitute for the function of HypA and vice versa. {ECO:0000269|PubMed:12081959}. EcoCyc product frame: EG11804-MONOMER. Genomic coordinates: 3139977-3140318. EcoCyc protein note: HybF and its homolog, HypA, are involved in the maturation of hydrogenase isozymes. HybF is required for maturation of hydrogenase isozymes 1 and 2, while HypA is involved in the maturation of hydrogenase 3; HypA and HybF can only partially substitute for each other . The presence of high levels of nickel can phenotypically rescue hypA and hybF mutants and a triple hypA hypB hybF mutant to a low level . Purified HybF contains Zn2+ in stoichiometric amounts. However, C89 in the C-terminal zinc finger motif is not essential for function of HybF. The protein is able to bind Ni2+ in vitro with a KD of 1.87 µM; a H2Q mutation drastically reduces Ni2+ binding. The H2 and E3 residues are also required for the hydrogenase maturation activity of HybF . Reviews:

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A703|protein.P0A703]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=hybF; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009818,ECOCYC:EG11804,GeneID:948004`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3139977-3140318:-; feature_type=gene

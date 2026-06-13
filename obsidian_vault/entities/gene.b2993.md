---
entity_id: "gene.b2993"
entity_type: "gene"
name: "hybD"
source_database: "NCBI RefSeq"
source_id: "gene-b2993"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2993"
  - "hybD"
---

# hybD

`gene.b2993`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2993`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hybD (gene.b2993) is a gene entity. It encodes hybD (protein.P37182). Encoded protein function: FUNCTION: Protease involved in the C-terminal processing of HybC, the large subunit of hydrogenase 2. Specifically cleaves off a 15 amino acid peptide from the C-terminus of the precursor of HybC. EcoCyc product frame: EG11802-MONOMER. Genomic coordinates: 3140792-3141286. EcoCyc protein note: HybD is an endopeptidase involved in the maturation of the large subunit of hydrogenase 2, HYBC-MONOMER HybC . Processing of HybC by HybD is dependent on prior insertion of Fe(CN)2CO. Processing of the HybC C terminus is required for assembly of the catalytically active HybC-HybO heterodimer . HybD was predicted to be the endopeptidase involved in the maturation of HybC based on its similarity to the processing enzyme for hydrogenase 3, HycI . In vitro maturation of FORMHYDROG2-CPLX with protein components including HybD has been achieved . Purified HybD does not contain stoichiometric amounts of bound metal ion . The crystal structure of HybD has been determined at 2.2 Å resolution . A ΔhybD mutant contains unprocessed HybC . Reviews:

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37182|protein.P37182]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=hybD; function=+

## External IDs

- `Dbxref:ASAP:ABE-0009826,ECOCYC:EG11802,GeneID:948982`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3140792-3141286:-; feature_type=gene

---
entity_id: "gene.b3510"
entity_type: "gene"
name: "hdeA"
source_database: "NCBI RefSeq"
source_id: "gene-b3510"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3510"
  - "hdeA"
---

# hdeA

`gene.b3510`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3510`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

hdeA (gene.b3510) is a gene entity. It encodes hdeA (protein.P0AES9). Encoded protein function: FUNCTION: Required for optimal acid stress protection. Exhibits a chaperone-like activity only at pH below 3 by suppressing non-specifically the aggregation of denaturated periplasmic proteins. Important for survival of enteric bacteria in the acidic environment of the host stomach. Also promotes the solubilization at neutral pH of proteins that had aggregated in their presence at acidic pHs. May cooperate with other periplasmic chaperones such as DegP and SurA. {ECO:0000269|PubMed:15911614, ECO:0000269|PubMed:17085547, ECO:0000269|PubMed:18359765, ECO:0000269|PubMed:21892184}. EcoCyc product frame: EG11398-MONOMER. EcoCyc synonyms: yhiB, yhhC. Genomic coordinates: 3656408-3656740. EcoCyc protein note: HdeA is an energy-independent chaperone that protects periplasmic proteins from acid-induced aggregation; HdeA is an acid-activated conditionally disordered chaperone (see ). HdeA is estimated to be highly abundant in both the growth and stationary phase; HdeA appears to form multimers . hdeA is non-essential for growth in both minimal and rich media; the phenotype of hdeA insertion mutants varies depending on the specific position and/or orientation of the marker...

## Biological Role

Repressed by hns (protein.P0ACF8), marA (protein.P0ACH5), fliZ (protein.P52627), gadW (protein.P63201). Activated by rpoD (protein.P00579), rpoS (protein.P13445), phoP (protein.P23836), gadW (protein.P63201), gadE (protein.P63204).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AES9|protein.P0AES9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (9)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=hdeA; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=hdeA; function=+
- `activates` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=hdeA; function=+
- `activates` <-- [[protein.P63201|protein.P63201]] `RegulonDB` `S` - regulator=GadW; target=hdeA; function=-+
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `C` - regulator=GadE; target=hdeA; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `C` - regulator=H-NS; target=hdeA; function=-
- `represses` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=hdeA; function=-
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `S` - regulator=FliZ; target=hdeA; function=-
- `represses` <-- [[protein.P63201|protein.P63201]] `RegulonDB` `S` - regulator=GadW; target=hdeA; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0011464,ECOCYC:EG11398,GeneID:948025`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3656408-3656740:-; feature_type=gene

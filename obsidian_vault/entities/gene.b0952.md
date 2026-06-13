---
entity_id: "gene.b0952"
entity_type: "gene"
name: "pqiC"
source_database: "NCBI RefSeq"
source_id: "gene-b0952"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0952"
  - "pqiC"
---

# pqiC

`gene.b0952`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0952`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

pqiC (gene.b0952) is a gene entity. It encodes pqiC (protein.P0AB10). Encoded protein function: FUNCTION: Component of a transport pathway that contributes to membrane integrity. {ECO:0000269|PubMed:27795327}. EcoCyc product frame: G6492-MONOMER. EcoCyc synonyms: ymbA. Genomic coordinates: 1014896-1015459. EcoCyc protein note: PqiC is a periplasmic facing, outer membrane lipoprotein; PqiC interacts with PqiB and the hetero-oligomer may bridge the inner and outer membrane; PqiC also forms homo-oligomers (see further ). pqiA, pqiB and pqiC form an operon; expression of a PqiC-PhoA fusion protein is induced by SoxC when exponentially growing cells are exposed to paraquat . pqiABC, letAB and ABC-45-CPLX "mlaFEDCB" are related loci; pqiABC (and letAB) are predicted to encode inter-membrane transport pathways that contribute to membrane integrity; simultaneous deletion of pqiABC and letAB in a ΔmlaD background increases sensitivity to EDTA and SDS; expression of pqiABC from a plasmid complements the SDS-EDTA hypersensitivity of a Δ(mlaD pqiB letB) strain; the substrate for transport is not known .

## Biological Role

Activated by rpoD (protein.P00579), soxS (protein.P0A9E2), marA (protein.P0ACH5), rpoS (protein.P13445).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AB10|protein.P0AB10]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (4)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=pqiC; function=+
- `activates` <-- [[protein.P0A9E2|protein.P0A9E2]] `RegulonDB` `C` - regulator=SoxS; target=pqiC; function=+
- `activates` <-- [[protein.P0ACH5|protein.P0ACH5]] `RegulonDB` `S` - regulator=MarA; target=pqiC; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=pqiC; function=+

## External IDs

- `Dbxref:ASAP:ABE-0003223,ECOCYC:G6492,GeneID:946972`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1014896-1015459:+; feature_type=gene

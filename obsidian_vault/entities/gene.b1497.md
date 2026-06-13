---
entity_id: "gene.b1497"
entity_type: "gene"
name: "ydeM"
source_database: "NCBI RefSeq"
source_id: "gene-b1497"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1497"
  - "ydeM"
---

# ydeM

`gene.b1497`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1497`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydeM (gene.b1497) is a gene entity. It encodes ydeM (protein.P76134). Encoded protein function: Anaerobic sulfatase-maturating enzyme homolog YdeM (AnSME homolog) EcoCyc product frame: G6787-MONOMER. Genomic coordinates: 1579633-1580790. EcoCyc protein note: YdeM is a member of the anaerobic sulfatase maturation enzyme subfamily of the Radical SAM superfamily of enzymes defined by . Both a ydeM single mutant and a aslB ydeM double null mutant are able to mature a heterologous sulfatase from Clostridium perfringens. Maturation of the C. perfringens enzyme appears to be dependent on a different enzyme that is present only under aerobic conditions . Expression of ydeNM is repressed by AraC in the presence of arabinose .

## Biological Role

Repressed by gadX (protein.P37639). Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76134|protein.P76134]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ydeM; function=+
- `represses` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=ydeM; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004986,ECOCYC:G6787,GeneID:945981`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1579633-1580790:-; feature_type=gene

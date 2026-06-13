---
entity_id: "gene.b1821"
entity_type: "gene"
name: "mntP"
source_database: "NCBI RefSeq"
source_id: "gene-b1821"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1821"
  - "mntP"
---

# mntP

`gene.b1821`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1821`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

mntP (gene.b1821) is a gene entity. It encodes mntP (protein.P76264). Encoded protein function: FUNCTION: Functions as a manganese exporter (PubMed:29440394, PubMed:38869303). Involved in manganese homeostasis (PubMed:21908668, PubMed:25774656, PubMed:29440394). Important for reducing the concentration of manganese in the cell when manganese levels are high, thus reducing its toxicity (PubMed:25774656). Transport of Mn(2+) by MntP is unlikely to be accompanied by an H(+) antiport (PubMed:38869303). Alters cellular resistance to reactive oxygen species (ROS) (PubMed:29440394). {ECO:0000269|PubMed:21908668, ECO:0000269|PubMed:25774656, ECO:0000269|PubMed:29440394, ECO:0000269|PubMed:38869303}. EcoCyc product frame: G6999-MONOMER. EcoCyc synonyms: yebN. Genomic coordinates: 1905688-1906254. EcoCyc protein note: mntP encodes the primary manganese exporter. An mntP deletion strain exhibits increased sensitivity to manganese and accumulates approximately 2-fold more intracellular manganese than the wild type . MntP confers robust manganese resistance; MntP expression affects resistance to reactive oxygen species; ectopic production of MntP halts the growth of a strain (ΔahpCF ΔkatG) that accumulates high levels of hydrogen peroxide . Inactivation of MntP increases the recovery of DNA replication after H2O2 exposure...

## Biological Role

Activated by rpoD (protein.P00579), fur (protein.P0A9A9).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76264|protein.P76264]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (2)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=mntP; function=+
- `activates` <-- [[protein.P0A9A9|protein.P0A9A9]] `RegulonDB` `S` - regulator=Fur; target=mntP; function=+

## External IDs

- `Dbxref:ASAP:ABE-0006065,ECOCYC:G6999,GeneID:946341`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1905688-1906254:+; feature_type=gene

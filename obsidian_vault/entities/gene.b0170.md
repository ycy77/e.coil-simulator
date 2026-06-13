---
entity_id: "gene.b0170"
entity_type: "gene"
name: "tsf"
source_database: "NCBI RefSeq"
source_id: "gene-b0170"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b0170"
  - "tsf"
---

# tsf

`gene.b0170`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b0170`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

tsf (gene.b0170) is a gene entity. It encodes tsf (protein.P0A6P1). Encoded protein function: FUNCTION: Associates with the EF-Tu.GDP complex and induces the exchange of GDP to GTP. It remains bound to the aminoacyl-tRNA.EF-Tu.GTP complex up to the GTP hydrolysis stage on the ribosome. {ECO:0000255|HAMAP-Rule:MF_00050}.; FUNCTION: (Microbial infection) In case of infection by bacteriophage Qbeta (and related Leviviruses), part of the viral RNA-dependent RNA polymerase complex. With EF-Tu may provide a stabilizing scaffold for the beta (catalytic) subunit, implicated in the elongation step of viral RNA synthesis where it fixes EF-Tu in an open conformation. {ECO:0000269|PubMed:20534494, ECO:0000269|PubMed:20798060, ECO:0000269|PubMed:22245970, ECO:0000269|PubMed:22884418, ECO:0000269|PubMed:25122749, ECO:0000269|PubMed:816798}.; FUNCTION: (Microbial infection) Promotes the tRNase activity of CdiA-CT from E.coli strain EC869 (CdiA-CT-EC869); required in vivo but less so in vitro. Probably loads charged tRNA onto EF-Tu, making more ternary GTP-EF-Tu-aa-tRNA complexes. The guanine nucleotide exchange factor capacity of this protein does not seem to be needed as no GTP hydrolysis occurs during tRNA cleavage. Also required in vivo for toxic activity of CdiA-CT from E.coli strains NC101 and CdiA-CT-96.154...

## Biological Role

Activated by rpoD (protein.P00579).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A6P1|protein.P0A6P1]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (1)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `C` - sigma=sigma70; target=tsf; function=+

## External IDs

- `Dbxref:ASAP:ABE-0000579,ECOCYC:EG11033,GeneID:944866`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:190857-191708:+; feature_type=gene

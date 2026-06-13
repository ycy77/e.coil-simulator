---
entity_id: "gene.b2196"
entity_type: "gene"
name: "ccmF"
source_database: "NCBI RefSeq"
source_id: "gene-b2196"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2196"
  - "ccmF"
---

# ccmF

`gene.b2196`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2196`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ccmF (gene.b2196) is a gene entity. It encodes ccmF (protein.P33927). Encoded protein function: FUNCTION: Required for the biogenesis of c-type cytochromes. Possible subunit of a heme lyase. EcoCyc product frame: EG12054-MONOMER. EcoCyc synonyms: yejR. Genomic coordinates: 2292961-2294904. EcoCyc protein note: CcmF and EG12052 CcmH are the components of holocytochrome c synthase in the System I pathway of cytochome c maturation; CcmFH releases heme from holoCCME-MONOMER CcmE and transfers it to apocytochromes in the periplasm. ccmF is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmF deletion mutant is able to produce (plasmid-encoded) mature Cytochromes-B b-type cytochrome and apocytochrome c-550 but not holocytochrome c-550 . Heme-containing CcmE accumulates in a mutant that is unable to synthesize CcmF . Release of heme from CcmE is blocked in the absence of CcmFGH proteins . CcmF interacts with CcmE and with CcmH but not with apocytochrome c (and see )...

## Biological Role

Repressed by narL (protein.P0AF28), narP (protein.P31802). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P33927|protein.P33927]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ccmF; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ccmF; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=ccmF; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmF; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ccmF; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmF; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007269,ECOCYC:EG12054,GeneID:948783`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2292961-2294904:-; feature_type=gene

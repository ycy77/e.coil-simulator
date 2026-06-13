---
entity_id: "gene.b2194"
entity_type: "gene"
name: "ccmH"
source_database: "NCBI RefSeq"
source_id: "gene-b2194"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2194"
  - "ccmH"
---

# ccmH

`gene.b2194`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2194`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ccmH (gene.b2194) is a gene entity. It encodes ccmH (protein.P0ABM9). Encoded protein function: FUNCTION: May be required for the biogenesis of c-type cytochromes. Possible subunit of a heme lyase. EcoCyc product frame: EG12052-MONOMER. EcoCyc synonyms: yejP. Genomic coordinates: 2291358-2292410. EcoCyc protein note: CcmH and EG12054-MONOMER CcmF are the components of holocytochrome c synthase in the System I pathway of cytochome c maturation; CcmFH releases heme from holoCCME-MONOMER CcmE and transfers it to apocytochromes in the periplasm. ccmH is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). CcmH is anchored to the membrane by two transmembrane regions; the protein contains an (essential) N-terminal periplasmic oxidoreductase domain containing the CXXC active site motif and a second (non-essential) C-terminal periplasmic domain containing tetratricopeptide repeat (TPR) motifs . The oxidized form of EG12053-MONOMER CcmG accumulates in mutants defective in CcmF...

## Biological Role

Repressed by narL (protein.P0AF28), narP (protein.P31802), nac (protein.Q47005). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABM9|protein.P0ABM9]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ccmH; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ccmH; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=ccmH; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmH; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ccmH; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmH; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ccmH; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007262,ECOCYC:EG12052,GeneID:946623`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2291358-2292410:-; feature_type=gene

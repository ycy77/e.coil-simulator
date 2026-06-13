---
entity_id: "gene.b2197"
entity_type: "gene"
name: "ccmE"
source_database: "NCBI RefSeq"
source_id: "gene-b2197"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2197"
  - "ccmE"
---

# ccmE

`gene.b2197`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2197`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ccmE (gene.b2197) is a gene entity. It encodes ccmE (protein.P69490). Encoded protein function: FUNCTION: Heme chaperone required for the biogenesis of c-type cytochromes. Transiently binds heme delivered by CcmC and transfers the heme to apo-cytochromes in a process facilitated by CcmF and CcmH. EcoCyc product frame: CCME-MONOMER. EcoCyc synonyms: yejS. Genomic coordinates: 2294901-2295380. EcoCyc protein note: CcmE is a membrane anchored, periplasmic heme chaperone that is required for PWY-8147 "cytochrome c biogenesis". ccmE is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmE deletion mutant cannot produce mature c-type cytochromes ; CcmE binds heme covalently via a conserved histidine residue (His-30) . Heme ligation in CcmE exhibits flexibility and it has been extensively studied (see ). The presence of apocytochrome c triggers release of heme from CcmE; heme release is blocked in the absence of CcmFGH (see also )...

## Biological Role

Repressed by narL (protein.P0AF28), narP (protein.P31802). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P69490|protein.P69490]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (6)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ccmE; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ccmE; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=ccmE; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmE; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ccmE; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmE; function=-+

## External IDs

- `Dbxref:ASAP:ABE-0007271,ECOCYC:EG12055,GeneID:946697`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2294901-2295380:-; feature_type=gene

---
entity_id: "gene.b2200"
entity_type: "gene"
name: "ccmB"
source_database: "NCBI RefSeq"
source_id: "gene-b2200"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b2200"
  - "ccmB"
---

# ccmB

`gene.b2200`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b2200`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ccmB (gene.b2200) is a gene entity. It encodes ccmB (protein.P0ABL8). Encoded protein function: FUNCTION: Required for the export of heme to the periplasm for the biogenesis of c-type cytochromes. EcoCyc product frame: CCMB-MONOMER. EcoCyc synonyms: yejV. Genomic coordinates: 2296362-2297024. EcoCyc protein note: CcmB is an integral membrane protein of the PWY-8147 "type I cytochrome c biogenesis system". ccmB is part of an 8 gene cluster (ccmABCDEFGH) which bears sequence similarity to Bradyrhizobium japonicum genes that are required for the biogenesis of Cytochromes-c "c-type cytochromes"; an E. coli ΔccmA-H mutant strain (EC06) is not able to produce mature c-type cytochromes under anaerobic, nonfermentative growth conditions (see also ). An in-frame ccmB deletion mutant cannot synthesize holocytochrome c but does produce heme-bound CCME-MONOMER CcmE (when CCMC-MONOMER CcmC is overproduced); CCMA-MONOMER CcmA and CcmB are implicated in heme transfer from holo-CcmE and attachment to apocytochrome c; CcmAB does not transport heme to the periplasm (and ). CcmB is predicted to be an integral membrane protein with six transmembrane helices; CcmA is detected in the membrane when CcmB is present and purified CcmAB has ATPase activity; inactivation of this activity does not abolish formation of holo-CcmE but does prevent production of c-type cytochromes...

## Biological Role

Repressed by narL (protein.P0AF28), narP (protein.P31802), nac (protein.Q47005). Activated by rpoD (protein.P00579), fnr (protein.P0A9E5), modE (protein.P0A9G8), narP (protein.P31802).

## Enriched Pathways

- `eco02010` ABC transporters (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0ABL8|protein.P0ABL8]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (7)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=ccmB; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `C` - regulator=FNR; target=ccmB; function=+
- `activates` <-- [[protein.P0A9G8|protein.P0A9G8]] `RegulonDB` `C` - regulator=ModE; target=ccmB; function=+
- `activates` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmB; function=-+
- `represses` <-- [[protein.P0AF28|protein.P0AF28]] `RegulonDB` `S` - regulator=NarL; target=ccmB; function=-
- `represses` <-- [[protein.P31802|protein.P31802]] `RegulonDB` `S` - regulator=NarP; target=ccmB; function=-+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=ccmB; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0007277,ECOCYC:EG12058,GeneID:946692`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:2296362-2297024:-; feature_type=gene

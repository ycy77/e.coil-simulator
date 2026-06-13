---
entity_id: "gene.b3860"
entity_type: "gene"
name: "dsbA"
source_database: "NCBI RefSeq"
source_id: "gene-b3860"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3860"
  - "dsbA"
---

# dsbA

`gene.b3860`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3860`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dsbA (gene.b3860) is a gene entity. It encodes dsbA (protein.P0AEG4). Encoded protein function: FUNCTION: Required for disulfide bond formation in some periplasmic proteins such as PhoA or OmpA. Acts by transferring its disulfide bond to other proteins and is reduced in the process. DsbA is reoxidized by DsbB. Required for pilus biogenesis. PhoP-regulated transcription is redox-sensitive, being activated when the periplasm becomes more reducing (deletion of dsbA/dsbB, treatment with dithiothreitol). MgrB acts between DsbA/DsbB and PhoP/PhoQ in this pathway. {ECO:0000269|PubMed:1429594, ECO:0000269|PubMed:22267510}. EcoCyc product frame: MONOMER0-4152. EcoCyc synonyms: dsf, iarA, ppfA. Genomic coordinates: 4043418-4044044. EcoCyc protein note: DsbA is a periplasmic thiol:disulfide oxidoreductase that promotes protein disulfide bond formation in E. coli K-12. DsbA contains a redox active disulfide bond (Cys30-Cys33) that is catalytically transferred via disulfide exchange to a diverse range of newly translocated protein substrates. Purified DsbA catalyses disulfide bond formation in in vitro translated alkaline phosphatase and stimulates the refolding of reduced bovine RNaseA . DsbA catalyses disulfide reduction in the presence of mild reducing agents in vitro - purified DsbA accelerates the reduction of insulin in the presence of dithiothreitol...

## Biological Role

Repressed by nac (protein.Q47005). Activated by rpoD (protein.P00579), cpxR (protein.P0AE88).

## Enriched Pathways

- `eco01503` Cationic antimicrobial peptide (CAMP) resistance (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0AEG4|protein.P0AEG4]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (3)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dsbA; function=+
- `activates` <-- [[protein.P0AE88|protein.P0AE88]] `RegulonDB` `S` - regulator=CpxR; target=dsbA; function=+
- `represses` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=dsbA; function=- | EcoCyc regulation TYPES=Transcription-Factor-Binding

## External IDs

- `Dbxref:ASAP:ABE-0012606,ECOCYC:EG11297,GeneID:948353`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:4043418-4044044:+; feature_type=gene

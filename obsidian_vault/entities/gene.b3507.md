---
entity_id: "gene.b3507"
entity_type: "gene"
name: "dctR"
source_database: "NCBI RefSeq"
source_id: "gene-b3507"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3507"
  - "dctR"
---

# dctR

`gene.b3507`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3507`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

dctR (gene.b3507) is a gene entity. It encodes dctR (protein.P37195). Encoded protein function: FUNCTION: May act as a transcriptional regulator of dctA. {ECO:0000269|PubMed:9811641}. EcoCyc product frame: EG11889-MONOMER. EcoCyc synonyms: yhiF. Genomic coordinates: 3654683-3655213. EcoCyc protein note: DctR is a predicted transcriptional regulator whose target may be dctA. A dctR mutation is the mechanism by which Suc+ reversion mutations suppress the growth defect on C4-dicarboxylates (such as succinate) that is exhibited by atp mutants . Like other transcriptional regulators, DctR forms heterodimers with RCSB-MONOMER RcsB, but does not appear to form homodimers. No regulatory targets have been identified yet . A slp dctR double mutation suppresses the increased acid resistance of a strain overproducing YdeO and affects survival in acidified spent minimal E glucose medium, indicating a role in protection against metabolic endproducts that are toxic at low pH . A slp-dctR double mutant exhibited loss of viability during growth in spent LB at pH 2.5 much faster than wild-type . The slp-dctR double mutant was also unable to survive at pH 2.5 in minimal medium when formate, succinate, or lactate were added...

## Biological Role

Repressed by hns (protein.P0ACF8). Activated by rpoD (protein.P00579), glaR (protein.P37338), gadX (protein.P37639), ydeO (protein.P76135).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P37195|protein.P37195]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=dctR; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=dctR; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `C` - regulator=GadX; target=dctR; function=+
- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=dctR; function=+
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=dctR; function=-

## External IDs

- `Dbxref:ASAP:ABE-0011454,ECOCYC:EG11889,GeneID:948021`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3654683-3655213:+; feature_type=gene

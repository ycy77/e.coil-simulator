---
entity_id: "gene.b1499"
entity_type: "gene"
name: "ydeO"
source_database: "NCBI RefSeq"
source_id: "gene-b1499"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1499"
  - "ydeO"
---

# ydeO

`gene.b1499`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1499`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

ydeO (gene.b1499) is a gene entity. It encodes ydeO (protein.P76135). Encoded protein function: FUNCTION: Induces the expression of gadE and mdtEF. Could also regulate the expression of other genes involved in acid resistance. {ECO:0000269|PubMed:12694615}. EcoCyc product frame: G6789-MONOMER. Genomic coordinates: 1582926-1583687. EcoCyc protein note: YdeO belongs to the AraC/XylS family of transcriptional regulators and shows more similarity to YhiW, AppY, AdiY, and GadX than the other AraC/XylS regulators . The members of this family exhibit two domains, an amino-terminal domain involved in coinducer recognition and dimerization and a carboxy-terminal domain that contains a potential helix-turn-helix DNA-binding motif . YdeO activates genes involved in the cellular response to acid resistance . This protein, together with the proteins HNS, EvgA, and GadE, pertains to a specific regulatory circuit that is functional in exponential-phase cells growing in minimal medium . Several of the genes directly regulated by YdeO are also directly regulated by GadX . The YdeO regulon has been determined . Based on ChIP-chip, RT-qPCR, EMSA, DNase I footprinting, and reporter assay, 7 new operons were identified as members of the YdeO regulon, including four stress response transcription factors, DctR, NhaR, GadE, and Gad, and several genes involved in respiration...

## Biological Role

Repressed by hns (protein.P0ACF8), phoP (protein.P23836), csrA (protein.P69913). Activated by evgA (protein.P0ACZ4), glaR (protein.P37338).

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P76135|protein.P76135]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (5)

- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=ydeO; function=+
- `activates` <-- [[protein.P37338|protein.P37338]] `RegulonDB|EcoCyc` `S` - regulator=GlaR; target=ydeO; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=ydeO; function=-
- `represses` <-- [[protein.P23836|protein.P23836]] `RegulonDB` `S` - regulator=PhoP; target=ydeO; function=-
- `represses` <-- [[protein.P69913|protein.P69913]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## External IDs

- `Dbxref:ASAP:ABE-0004992,ECOCYC:G6789,GeneID:945922`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1582926-1583687:-; feature_type=gene

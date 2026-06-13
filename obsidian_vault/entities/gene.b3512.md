---
entity_id: "gene.b3512"
entity_type: "gene"
name: "gadE"
source_database: "NCBI RefSeq"
source_id: "gene-b3512"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b3512"
  - "gadE"
---

# gadE

`gene.b3512`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b3512`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gadE (gene.b3512) is a gene entity. It encodes gadE (protein.P63204). Encoded protein function: FUNCTION: Regulates the expression of several genes involved in acid resistance. Required for the expression of gadA and gadBC, among others, regardless of media or growth conditions. Binds directly to the 20 bp GAD box found in the control regions of both loci. {ECO:0000269|PubMed:12940989, ECO:0000269|PubMed:14702398}. EcoCyc product frame: EG11544-MONOMER. EcoCyc synonyms: yhiE, yhiT. Genomic coordinates: 3658366-3658893. EcoCyc protein note: The transcriptional activator GadE, for "Glutamic acid decarboxylase," is positively autoregulated and controls the transcription of genes involved in the maintenance of pH homeostasis, including the principal acid resistance system , glutamate dependent (GAD), also referred as the GAD system, and genes involved in multidrug efflux, among others . GadE also controls the expression of two transcription factors related to acid resistance, GadW and GadX, and for this reason it is considered the central activator of the acid response system . GadE is encoded by the gadE-mdtEF operon, inducible by low pH , which is located in the region called the acid fitness island . Expression of gadE is controlled by an unusually large 798-bp upstream intergenic region, termed the sensory integration locus...

## Biological Role

Repressed by hns (protein.P0ACF8), crp (protein.P0ACJ8), fliZ (protein.P52627), csrA (protein.P69913). Activated by rpoD (protein.P00579), arcA (protein.P0A9Q1), evgA (protein.P0ACZ4), rpoS (protein.P13445), gadX (protein.P37639), gadE (protein.P63204), ydeO (protein.P76135), nac (protein.Q47005), and 1 more.

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63204|protein.P63204]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (13)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gadE; function=+
- `activates` <-- [[protein.P0A9Q1|protein.P0A9Q1]] `RegulonDB` `S` - regulator=ArcA; target=gadE; function=+
- `activates` <-- [[protein.P0ACZ4|protein.P0ACZ4]] `RegulonDB` `S` - regulator=EvgA; target=gadE; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=gadE; function=+
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=gadE; function=+
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `S` - regulator=GadE; target=gadE; function=+
- `activates` <-- [[protein.P76135|protein.P76135]] `RegulonDB` `S` - regulator=YdeO; target=gadE; function=+
- `activates` <-- [[protein.Q47005|protein.Q47005]] `RegulonDB|EcoCyc` `S` - regulator=Nac; target=gadE; function=+ | EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.ecocyc.PHOSPHO-TORR|protein.ecocyc.PHOSPHO-TORR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `RegulonDB` `S` - regulator=H-NS; target=gadE; function=-
- `represses` <-- [[protein.P0ACJ8|protein.P0ACJ8]] `RegulonDB` `S` - regulator=CRP; target=gadE; function=-
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `C` - regulator=FliZ; target=gadE; function=-
- `represses` <-- [[protein.P69913|protein.P69913]] `EcoCyc` `database` - EcoCyc regulation TYPES=Protein-Mediated-Translation-Regulation

## External IDs

- `Dbxref:ASAP:ABE-0011475,ECOCYC:EG11544,GeneID:948023`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:3658366-3658893:+; feature_type=gene

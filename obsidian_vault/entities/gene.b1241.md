---
entity_id: "gene.b1241"
entity_type: "gene"
name: "adhE"
source_database: "NCBI RefSeq"
source_id: "gene-b1241"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1241"
  - "adhE"
---

# adhE

`gene.b1241`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1241`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

adhE (gene.b1241) is a gene entity. It encodes adhE (protein.P0A9Q7). Encoded protein function: FUNCTION: Under fermentative conditions, catalyzes the sequential NADH-dependent reduction of acetyl-CoA to acetaldehyde and then to ethanol (PubMed:10612730, PubMed:10922373, PubMed:17280641, PubMed:2015910, PubMed:6752127). Under aerobic conditions, despite the reversibility of the two NADH-coupled reactions, wild-type E.coli cannot grow on ethanol as the sole carbon and energy source due to the down-regulation of adhE transcription and the inactivation of the enzyme by metal-catalyzed oxidation (MCO) (PubMed:10922373). Nevertheless, in the presence of oxygen, AdhE may act as a hydrogen peroxide scavenger and have a protective role against oxidative stress (PubMed:12783863). {ECO:0000269|PubMed:10612730, ECO:0000269|PubMed:10922373, ECO:0000269|PubMed:12783863, ECO:0000269|PubMed:17280641, ECO:0000269|PubMed:2015910, ECO:0000269|PubMed:6752127}. EcoCyc product frame: ADHE-MONOMER. EcoCyc synonyms: adhC, ana. Genomic coordinates: 1295446-1298121. EcoCyc protein note: Under anaerobic conditions, the multifunctional enzyme AdhE catalyzes the sequential reduction of acetyl-CoA to acetaldehyde and then to ethanol (see the FERMENTATION-PWY pathway)...

## Biological Role

Repressed by cra (protein.P0ACP1). Activated by FlhDC DNA-binding transcriptional dual regulator (complex.ecocyc.CPLX0-3930), DNA-binding transcriptional dual regulator FNR (complex.ecocyc.CPLX0-7797), fis (protein.P0A6R3), fnr (protein.P0A9E5), lrp (protein.P0ACJ0), rpoS (protein.P13445), ygfI (protein.P52044).

## Enriched Pathways

- `eco00010` Glycolysis / Gluconeogenesis (KEGG)
- `eco00071` Fatty acid degradation (KEGG)
- `eco00350` Tyrosine metabolism (KEGG)
- `eco00620` Pyruvate metabolism (KEGG)
- `eco00625` Chloroalkane and chloroalkene degradation (KEGG)
- `eco00626` Naphthalene degradation (KEGG)
- `eco00650` Butanoate metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01110` Biosynthesis of secondary metabolites (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)
- `eco01220` Degradation of aromatic compounds (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P0A9Q7|protein.P0A9Q7]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (8)

- `activates` <-- [[complex.ecocyc.CPLX0-3930|complex.ecocyc.CPLX0-3930]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[complex.ecocyc.CPLX0-7797|complex.ecocyc.CPLX0-7797]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P0A6R3|protein.P0A6R3]] `RegulonDB` `S` - regulator=Fis; target=adhE; function=+
- `activates` <-- [[protein.P0A9E5|protein.P0A9E5]] `RegulonDB` `S` - regulator=FNR; target=adhE; function=+
- `activates` <-- [[protein.P0ACJ0|protein.P0ACJ0]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=adhE; function=+
- `activates` <-- [[protein.P52044|protein.P52044]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACP1|protein.P0ACP1]] `RegulonDB` `C` - regulator=Cra; target=adhE; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004164,ECOCYC:EG10031,GeneID:945837`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1295446-1298121:-; feature_type=gene

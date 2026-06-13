---
entity_id: "gene.b1492"
entity_type: "gene"
name: "gadC"
source_database: "NCBI RefSeq"
source_id: "gene-b1492"
default_state: "expressed"
allowed_states: "expressed|repressed|knocked_out|mutated|overexpressed"
subcellular_location: "cytosol"
enriched_summary_quality: "informative"
tags:
  - entity/gene
  - source/NCBI_RefSeq
aliases:
  - "b1492"
  - "gadC"
---

# gadC

`gene.b1492`

## Static

- Type: `gene`
- Source: `NCBI RefSeq:gene-b1492`
- Default state: `expressed`
- Allowed states: `expressed|repressed|knocked_out|mutated|overexpressed`
- Location: cytosol

## Enriched Summary

gadC (gene.b1492) is a gene entity. It encodes gadC (protein.P63235). Encoded protein function: FUNCTION: Involved in glutaminase-dependent acid resistance (PubMed:30498489, PubMed:8682809). Exchanges extracellular glutamate (Glu) for intracellular gamma-aminobutyric acid (GABA) under acidic conditions (PubMed:22407317, PubMed:23589309). The protonation states of substrates are crucial for transport. Selectively transports Glu with no net charge and GABA with a positive charge (PubMed:23589309). Also efficiently transports glutamine and, to a smaller extent, methionine and leucine (PubMed:22407317). When the extracellular pH drops below 2.5, can import L-glutamine and export either glutamate or GABA (PubMed:30498489). The ability to survive the extremely acidic conditions of the stomach is essential for successful colonization of the host by commensal and pathogenic bacteria (PubMed:30498489, PubMed:8682809). {ECO:0000269|PubMed:22407317, ECO:0000269|PubMed:23589309, ECO:0000269|PubMed:30498489, ECO:0000269|PubMed:8682809, ECO:0000305|PubMed:30498489, ECO:0000305|PubMed:8682809}. EcoCyc product frame: XASA-MONOMER. EcoCyc synonyms: acsA, xasA. Genomic coordinates: 1568954-1570489. EcoCyc protein note: GadC, a glutamic acid:γ-aminobutyrate antiporter, is part of the glutamate-dependent acid resistance system 2 (AR2) which confers resistance to extreme acid conditions...

## Biological Role

Repressed by hns (protein.P0ACF8), fliZ (protein.P52627), gadW (protein.P63201), csrA (protein.P69913). Activated by rpoD (protein.P00579), rpoS (protein.P13445), adiY (protein.P33234), gadX (protein.P37639), gadW (protein.P63201), gadE (protein.P63204), DNA-binding transcriptional dual regulator TorR-phosphorylated (protein.ecocyc.PHOSPHO-TORR).

## Enriched Pathways

- `eco02024` Quorum sensing (KEGG)

## Annotation

NCBI RefSeq gene feature

## Outgoing Edges (1)

- `encodes` --> [[protein.P63235|protein.P63235]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## Incoming Edges (11)

- `activates` <-- [[protein.P00579|protein.P00579]] `RegulonDB` `S` - sigma=sigma70; target=gadC; function=+
- `activates` <-- [[protein.P13445|protein.P13445]] `RegulonDB` `S` - sigma=sigma38; target=gadC; function=+
- `activates` <-- [[protein.P33234|protein.P33234]] `RegulonDB` `S` - regulator=AdiY; target=gadC; function=+
- `activates` <-- [[protein.P37639|protein.P37639]] `RegulonDB` `S` - regulator=GadX; target=gadC; function=+
- `activates` <-- [[protein.P63201|protein.P63201]] `RegulonDB` `S` - regulator=GadW; target=gadC; function=-+
- `activates` <-- [[protein.P63204|protein.P63204]] `RegulonDB` `C` - regulator=GadE; target=gadC; function=+
- `activates` <-- [[protein.ecocyc.PHOSPHO-TORR|protein.ecocyc.PHOSPHO-TORR]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P0ACF8|protein.P0ACF8]] `EcoCyc` `database` - EcoCyc regulation TYPES=Transcription-Factor-Binding
- `represses` <-- [[protein.P52627|protein.P52627]] `RegulonDB` `S` - regulator=FliZ; target=gadC; function=-
- `represses` <-- [[protein.P63201|protein.P63201]] `RegulonDB` `S` - regulator=GadW; target=gadC; function=-+
- `represses` <-- [[protein.P69913|protein.P69913]] `RegulonDB` `S` - regulator=CsrA; target=gadC; function=-

## External IDs

- `Dbxref:ASAP:ABE-0004973,ECOCYC:G6786,GeneID:946057`
- `gbkey:Gene`
- `gene_biotype:protein_coding`

## Notes

NC_000913.3:1568954-1570489:-; feature_type=gene

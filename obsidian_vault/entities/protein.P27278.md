---
entity_id: "protein.P27278"
entity_type: "protein"
name: "nadR"
source_database: "UniProt"
source_id: "P27278"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein. Cytoplasm {ECO:0000250}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nadR nadI b4390 JW5800"
---

# nadR

`protein.P27278`

## Static

- Type: `protein`
- Source: `UniProt:P27278`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane; Peripheral membrane protein. Cytoplasm {ECO:0000250}.

## Enriched Summary

FUNCTION: This enzyme has three activities: DNA binding, nicotinamide mononucleotide (NMN) adenylyltransferase and ribosylnicotinamide (RN) kinase. The DNA-binding domain binds to the nadB operator sequence in an NAD- and ATP-dependent manner. As NAD levels increase within the cell, the affinity of NadR for the nadB operator regions of nadA, nadB, and pncB increases, repressing the transcription of these genes. The RN kinase activity catalyzes the phosphorylation of RN to form nicotinamide ribonucleotide. The NMN adenylyltransferase activity catalyzes the transfer of the AMP moiety of ATP to nicotinamide ribonucleotide to form NAD(+). The NMN adenylyltransferase domain also functions as the NAD and ATP sensor. {ECO:0000269|PubMed:10464228}.

## Biological Role

Catalyzes ATP:nicotinamide-nucleotide adenylyltransferase (reaction.R00137). Component of DNA-binding transcriptional repressor/NMN adenylyltransferase NadR (complex.ecocyc.CPLX0-7975).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: This enzyme has three activities: DNA binding, nicotinamide mononucleotide (NMN) adenylyltransferase and ribosylnicotinamide (RN) kinase. The DNA-binding domain binds to the nadB operator sequence in an NAD- and ATP-dependent manner. As NAD levels increase within the cell, the affinity of NadR for the nadB operator regions of nadA, nadB, and pncB increases, repressing the transcription of these genes. The RN kinase activity catalyzes the phosphorylation of RN to form nicotinamide ribonucleotide. The NMN adenylyltransferase activity catalyzes the transfer of the AMP moiety of ATP to nicotinamide ribonucleotide to form NAD(+). The NMN adenylyltransferase domain also functions as the NAD and ATP sensor. {ECO:0000269|PubMed:10464228}.

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (3)

- `catalyzes` --> [[reaction.R00137|reaction.R00137]] `KEGG` `database` - via EC:2.7.7.1
- `is_component_of` --> [[complex.ecocyc.CPLX0-7975|complex.ecocyc.CPLX0-7975]] `EcoCyc` `database` - EcoCyc component coefficient=4 | EcoCyc protcplxs.col coefficient=4
- `represses` --> [[gene.b2574|gene.b2574]] `RegulonDB` `S` - regulator=NadR; target=nadB; function=-

## Incoming Edges (1)

- `encodes` <-- [[gene.b4390|gene.b4390]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P27278`
- `KEGG:ecj:JW5800;eco:b4390;ecoc:C3026_23720;`
- `GeneID:75169885;948911;`
- `GO:GO:0000287; GO:0000309; GO:0000987; GO:0005524; GO:0005737; GO:0005886; GO:0009435; GO:0010446; GO:0042802; GO:0050262; GO:0051289; GO:0071248; GO:1902494; GO:1902503`
- `EC:2.7.1.22; 2.7.7.1`

## Notes

Trifunctional NAD biosynthesis/regulator protein NadR [Includes: Transcriptional regulator NadR; Nicotinamide mononucleotide adenylyltransferase (NMN adenylyltransferase) (NMN-AT) (NMNAT) (EC 2.7.7.1) (Nicotinamide ribonucleotide adenylyltransferase) (Nicotinamide-nucleotide adenylyltransferase); Ribosylnicotinamide kinase (RNK) (EC 2.7.1.22) (Nicotinamide riboside kinase) (NRK) (NmR-K)]

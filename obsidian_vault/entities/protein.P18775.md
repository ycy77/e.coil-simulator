---
entity_id: "protein.P18775"
entity_type: "protein"
name: "dmsA"
source_database: "UniProt"
source_id: "P18775"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:2170332, ECO:0000269|PubMed:3280546}; Peripheral membrane protein {ECO:0000269|PubMed:2170332, ECO:0000269|PubMed:3280546}; Cytoplasmic side {ECO:0000269|PubMed:2170332, ECO:0000269|PubMed:3280546}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "dmsA b0894 JW5118"
---

# dmsA

`protein.P18775`

## Static

- Type: `protein`
- Source: `UniProt:P18775`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cell membrane {ECO:0000269|PubMed:2170332, ECO:0000269|PubMed:3280546}; Peripheral membrane protein {ECO:0000269|PubMed:2170332, ECO:0000269|PubMed:3280546}; Cytoplasmic side {ECO:0000269|PubMed:2170332, ECO:0000269|PubMed:3280546}.

## Enriched Summary

FUNCTION: Catalyzes the reduction of dimethyl sulfoxide (DMSO) to dimethyl sulfide (DMS). DMSO reductase serves as the terminal reductase under anaerobic conditions, with DMSO being the terminal electron acceptor. Terminal reductase during anaerobic growth on various sulfoxides and N-oxide compounds. Allows E.coli to grow anaerobically on DMSO as respiratory oxidant. {ECO:0000269|PubMed:3062312}. The DmsA subunit of DMSO reductase contains a molybdo-bis(pyranopterin guanine dinucleotide) (Mo-bisPGD) cofactor and a [4Fe-4S] cluster (known as FS0) . DmsA contains a twin-arginine leader peptide which targets the protein to the membrane, although DmsA does not appear to be exported to the periplasm. The leader peptide is also essential for expression of DmsA and stability of the DmsAB dimer, and is cleaved between residues 45 and 46 . The leader peptide interacts with the redox enzyme maturation protein (REMP) G6849-MONOMER "DmsD" .

## Biological Role

Component of dimethyl sulfoxide reductase (complex.ecocyc.DIMESULFREDUCT-CPLX).

## Enriched Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Annotation

FUNCTION: Catalyzes the reduction of dimethyl sulfoxide (DMSO) to dimethyl sulfide (DMS). DMSO reductase serves as the terminal reductase under anaerobic conditions, with DMSO being the terminal electron acceptor. Terminal reductase during anaerobic growth on various sulfoxides and N-oxide compounds. Allows E.coli to grow anaerobically on DMSO as respiratory oxidant. {ECO:0000269|PubMed:3062312}.

## Pathways

- `eco00920` Sulfur metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01120` Microbial metabolism in diverse environments (KEGG)

## Outgoing Edges (2)

- `is_component_of` --> [[complex.ecocyc.DIMESULFREDUCT-CPLX|complex.ecocyc.DIMESULFREDUCT-CPLX]] `EcoCyc` `database` - EcoCyc component coefficient=1 | EcoCyc protcplxs.col coefficient=1
- `represses` --> [[reaction.ecocyc.RXN-19619|reaction.ecocyc.RXN-19619]] `EcoCyc` `database` - EcoCyc regulation TYPES=Regulation-of-Enzyme-Activity

## Incoming Edges (1)

- `encodes` <-- [[gene.b0894|gene.b0894]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P18775`
- `KEGG:ecj:JW5118;eco:b0894;ecoc:C3026_05530;`
- `GeneID:75170969;945508;`
- `GO:GO:0005886; GO:0009055; GO:0009061; GO:0009389; GO:0009390; GO:0018907; GO:0019645; GO:0030151; GO:0030288; GO:0033797; GO:0043546; GO:0051539`
- `EC:1.8.5.3`

## Notes

Dimethyl sulfoxide reductase DmsA (DMSO reductase) (DMSOR) (Me2SO reductase) (EC 1.8.5.3)

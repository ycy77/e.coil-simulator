---
entity_id: "protein.Q46810"
entity_type: "protein"
name: "mocA"
source_database: "UniProt"
source_id: "Q46810"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "mocA ygfJ b2877 JW2845"
---

# mocA

`protein.Q46810`

## Static

- Type: `protein`
- Source: `UniProt:Q46810`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Transfers a CMP moiety from CTP to Mo-molybdopterin (Mo-MPT) cofactor (Moco or molybdenum cofactor) to form Mo-molybdopterin cytosine dinucleotide (Mo-MCD) cofactor. Is specific for CTP; other nucleotides such as ATP and GTP cannot be utilized. Is also able to convert MPT to MCD in the absence of molybdate, however, with only one catalytic turnover. {ECO:0000269|PubMed:19542235}. MocA is a molybdenum cofactor cytidylyltransferase belonging to the NTP transferase superfamily of proteins. The enzyme catalyzes the transfer of a CMP moiety from CTP to Mo-molybdopterin, forming MCD . The specificity of MocA for CTP was also investigated, showing that the N-terminal domain determines nucleotide recognition and binding. The C-terminal domain is responsible for interacting with the specific acceptor protein G6154-MONOMER PaoD . A mocA mutant contains inactive CPLX0-7805 lacking molybdenum and is thus unable to grow on medium containing cinnamaldehyde . Reviews:

## Biological Role

Catalyzes RXN0-6254 (reaction.ecocyc.RXN0-6254). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Annotation

FUNCTION: Transfers a CMP moiety from CTP to Mo-molybdopterin (Mo-MPT) cofactor (Moco or molybdenum cofactor) to form Mo-molybdopterin cytosine dinucleotide (Mo-MCD) cofactor. Is specific for CTP; other nucleotides such as ATP and GTP cannot be utilized. Is also able to convert MPT to MCD in the absence of molybdate, however, with only one catalytic turnover. {ECO:0000269|PubMed:19542235}.

## Pathways

- `eco00790` Folate biosynthesis (KEGG)
- `eco01100` Metabolic pathways (KEGG)

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-6254|reaction.ecocyc.RXN0-6254]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b2877|gene.b2877]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:Q46810`
- `KEGG:ecj:JW2845;eco:b2877;ecoc:C3026_15780;`
- `GeneID:947356;`
- `GO:GO:0000166; GO:0000287; GO:0006777; GO:0061602; GO:1902760`
- `EC:2.7.7.76`

## Notes

Molybdenum cofactor cytidylyltransferase (MoCo cytidylyltransferase) (EC 2.7.7.76) (CTP:molybdopterin cytidylyltransferase) (Mo-MPT cytidylyltransferase) (Molybdopterin cytidylyltransferase) (Molybdopterin-cytosine dinucleotide synthase) (MCD synthase)

---
entity_id: "protein.P0A752"
entity_type: "protein"
name: "nadD"
source_database: "UniProt"
source_id: "P0A752"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: ""
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "nadD ybeN b0639 JW0634"
---

# nadD

`protein.P0A752`

## Static

- Type: `protein`
- Source: `UniProt:P0A752`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`

## Enriched Summary

FUNCTION: Catalyzes the reversible adenylation of nicotinate mononucleotide (NaMN) to nicotinic acid adenine dinucleotide (NaAD). {ECO:0000269|PubMed:10894752}. Nicotinate-mononucleotide adenylyltransferase (NadD) is an essential enzyme involved in both de novo biosynthesis and salvage of NAD+ . Its essentiality makes it a target for the development of antibacterial agents . Both nicotinic acid mononucleotide (NaMN) and nicotinamide mononucleotide (NMN) are substrates, but the rate of adenylation of NaMN is at least 20 times faster than that of NMN . Crystal structures of the enzyme alone and in a complex with deamido-NAD have been solved and show that ligand binding causes conformational changes in regions surrounding the active site . nadD is essential for growth . The nadD72 mutant allele was first isolated as a spontaneous temperature-sensitive mutation that leads to higher tolerance to fusidic acid. The mutant phenotype is pleiotropic . Further characterization of this mutation showed it to be an allele of nadD with a -1 frameshift mutation that leads to a change in the C terminus of the NadD protein. The mutant synthesizes very little NAD+ and NADPH at the permissive temperature and essentially none at the non-permissive temperature . The newly isolated nadD74 allele causes an amino acid change in the ATP-binding site of NadD...

## Biological Role

Catalyzes ATP:nicotinamide-nucleotide adenylyltransferase (reaction.R00137), NICONUCADENYLYLTRAN-RXN (reaction.ecocyc.NICONUCADENYLYLTRAN-RXN). Bound by Magnesium cation (molecule.C00305).

## Enriched Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Annotation

FUNCTION: Catalyzes the reversible adenylation of nicotinate mononucleotide (NaMN) to nicotinic acid adenine dinucleotide (NaAD). {ECO:0000269|PubMed:10894752}.

## Pathways

- `eco00760` Nicotinate and nicotinamide metabolism (KEGG)
- `eco01100` Metabolic pathways (KEGG)
- `eco01240` Biosynthesis of cofactors (KEGG)

## Outgoing Edges (2)

- `catalyzes` --> [[reaction.R00137|reaction.R00137]] `KEGG` `database` - via EC:2.7.7.18
- `catalyzes` --> [[reaction.ecocyc.NICONUCADENYLYLTRAN-RXN|reaction.ecocyc.NICONUCADENYLYLTRAN-RXN]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (2)

- `binds` <-- [[molecule.C00305|molecule.C00305]] `EcoCyc` `database` - EcoCyc enzymatic reaction cofactor
- `encodes` <-- [[gene.b0639|gene.b0639]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0A752`
- `KEGG:ecj:JW0634;eco:b0639;ecoc:C3026_03195;`
- `GeneID:93776843;945248;`
- `GO:GO:0000309; GO:0004515; GO:0005524; GO:0009435; GO:0034355; GO:0034628`
- `EC:2.7.7.18`

## Notes

Nicotinate-nucleotide adenylyltransferase (EC 2.7.7.18) (Deamido-NAD(+) diphosphorylase) (Deamido-NAD(+) pyrophosphorylase) (Nicotinate mononucleotide adenylyltransferase) (NaMN adenylyltransferase)

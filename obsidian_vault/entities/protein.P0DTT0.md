---
entity_id: "protein.P0DTT0"
entity_type: "protein"
name: "bipA"
source_database: "UniProt"
source_id: "P0DTT0"
default_state: "active"
allowed_states: "active|inhibited|degraded|sequestered"
subcellular_location: "SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00849, ECO:0000269|PubMed:30305394, ECO:0000269|Ref.12}. Note=Associates with 70S ribosomes and 30S and 50S subunits in the presence of GMPPNP (a nonhydrolyzable GTP analog) at both 20 and 37 degrees Celsius; no change in ribosome association is seen in the presence of ppGpp or when the stringent response is triggered. {ECO:0000269|PubMed:30305394}."
enriched_summary_quality: "informative"
tags:
  - entity/protein
  - source/UniProt
aliases:
  - "bipA o591 typA yihK b3871 JW5571"
---

# bipA

`protein.P0DTT0`

## Static

- Type: `protein`
- Source: `UniProt:P0DTT0`
- Default state: `active`
- Allowed states: `active|inhibited|degraded|sequestered`
- Location: SUBCELLULAR LOCATION: Cytoplasm {ECO:0000255|HAMAP-Rule:MF_00849, ECO:0000269|PubMed:30305394, ECO:0000269|Ref.12}. Note=Associates with 70S ribosomes and 30S and 50S subunits in the presence of GMPPNP (a nonhydrolyzable GTP analog) at both 20 and 37 degrees Celsius; no change in ribosome association is seen in the presence of ppGpp or when the stringent response is triggered. {ECO:0000269|PubMed:30305394}.

## Enriched Summary

FUNCTION: A 50S ribosomal subunit assembly protein with GTPase and nucleotide-independent chaperone activity, required for 50S subunit assembly at low temperatures, may also play a role in translation (PubMed:30305394). Genetic and deletion evidence suggests this is involved in ribosome assembly at low temperatures; it may also affect translation (Probable) (PubMed:25777676, PubMed:30305394). Involved in incorporation of ribosomal protein uL6 into precursor 44S ribosomal particles at low temperatures. Also has chaperone activity which does not require nucleotides (PubMed:30305394). Binds GDP, ppGpp and GDPCP (a nonhydrolyzable GTP analog) with similar affinity; the conformation of the protein does not significantly change upon nucleotide binding (PubMed:26163516, PubMed:26283392). Interacts with ribosomes (PubMed:26283392, Ref.12). Binds the 70S ribosome between the 30S and 50S subunits, in a similar position as ribosome-bound EF-G; it contacts a number of ribosomal proteins, both rRNAs and the A-site tRNA. Ribosome binding alters its conformation (PubMed:26283392). Genetically its function does not overlap LepA, and it acts in a different pathway during ribosome assembly than does RNA helicase DeaD (PubMed:25777676). GTPase that affects interactions between enteropathogenic E.coli (EPEC) and epithelial cells (PubMed:9622352)...

## Biological Role

Catalyzes RXN0-5462 (reaction.ecocyc.RXN0-5462).

## Annotation

FUNCTION: A 50S ribosomal subunit assembly protein with GTPase and nucleotide-independent chaperone activity, required for 50S subunit assembly at low temperatures, may also play a role in translation (PubMed:30305394). Genetic and deletion evidence suggests this is involved in ribosome assembly at low temperatures; it may also affect translation (Probable) (PubMed:25777676, PubMed:30305394). Involved in incorporation of ribosomal protein uL6 into precursor 44S ribosomal particles at low temperatures. Also has chaperone activity which does not require nucleotides (PubMed:30305394). Binds GDP, ppGpp and GDPCP (a nonhydrolyzable GTP analog) with similar affinity; the conformation of the protein does not significantly change upon nucleotide binding (PubMed:26163516, PubMed:26283392). Interacts with ribosomes (PubMed:26283392, Ref.12). Binds the 70S ribosome between the 30S and 50S subunits, in a similar position as ribosome-bound EF-G; it contacts a number of ribosomal proteins, both rRNAs and the A-site tRNA. Ribosome binding alters its conformation (PubMed:26283392). Genetically its function does not overlap LepA, and it acts in a different pathway during ribosome assembly than does RNA helicase DeaD (PubMed:25777676). GTPase that affects interactions between enteropathogenic E.coli (EPEC) and epithelial cells (PubMed:9622352). Probably regulates expression of proteins required for (at least) K5 polysaccharide production (Probable) (PubMed:10781541). Deletion mutants of bipA are suppressed by an rluC deletion, which no longer modifies uracils 955, 2504 and 2580 to pseudouridine in 23S rRNA; there are 5 other pseudouridine synthases in E.coli, only rluC suppresses this phenotype. Mutating 23S rRNA so the 3 uracils are other nucleotides also suppresses the bipA deletion; pseudouridine-2504 is required for ribosome assembly and translational accuracy (PubMed:18820021, PubMed:25777676). {ECO:0000269|PubMed:18820021, ECO:0000269|PubMed:25777676, ECO:0000269|PubMed:26163516, ECO:0000269|PubMed:26283392, ECO:0000269|PubMed:30305394, ECO:0000269|PubMed:9622352, ECO:0000269|Ref.12, ECO:0000305|PubMed:10781541, ECO:0000305|PubMed:18820021}.

## Outgoing Edges (1)

- `catalyzes` --> [[reaction.ecocyc.RXN0-5462|reaction.ecocyc.RXN0-5462]] `EcoCyc` `database` - EcoCyc enzymatic reaction

## Incoming Edges (1)

- `encodes` <-- [[gene.b3871|gene.b3871]] `UniProt|EcoCyc` `database` - EcoCyc gene PRODUCT

## External IDs

- `UniProt:P0DTT0`
- `KEGG:ecj:JW5571;eco:b3871;ecoc:C3026_20930;`
- `GeneID:93778065;948369;`
- `GO:GO:0000027; GO:0000049; GO:0003924; GO:0005525; GO:0005829; GO:0006412; GO:0009408; GO:0009409; GO:0019843; GO:0043022; GO:0044183; GO:0097216; GO:1990904`
- `EC:3.6.5.-`

## Notes

Large ribosomal subunit assembly factor BipA (EC 3.6.5.-) (50S ribosomal subunit assembly factor BipA) (GTP-binding protein BipA/TypA) (Ribosome assembly factor BipA) (Ribosome-dependent GTPase BipA) (Tyrosine phosphorylated protein A)
